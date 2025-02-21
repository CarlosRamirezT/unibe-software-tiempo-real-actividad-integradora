import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from backend.data_capture import events, events_lock

def start_ui():
    root = tk.Tk()
    root.title("Monitoreo en Tiempo Real de Actividad")
    root.geometry("800x600")
    root.configure(bg="white")

    # Frame para el gráfico (parte superior)
    chart_frame = tk.Frame(root, bg="white")
    chart_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=False)

    # Frame para el log (parte inferior)
    log_frame = tk.Frame(root, bg="white")
    log_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    # Crear la figura y eje para el gráfico, con fondo blanco
    fig, ax = plt.subplots(figsize=(8, 3))
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Widget de texto para el log, con fondo y texto definidos
    text_area = ScrolledText(log_frame, wrap=tk.WORD, width=100, height=20,
                               bg="white", fg="black")
    text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    def update_chart():
        # Copia la lista de eventos de forma segura
        events_lock.acquire()
        try:
            events_copy = events.copy()
        finally:
            events_lock.release()

        totals = {}
        for ev in events_copy:
            ev_type = ev.get("type", "unknown")
            totals[ev_type] = totals.get(ev_type, 0) + 1

        ax.clear()
        if totals:
            labels = list(totals.keys())
            values = list(totals.values())
            ax.bar(labels, values, color='skyblue')
            ax.set_title("Totales de Eventos por Tipo (Tiempo Real)", color="black")
            ax.set_ylabel("Cantidad", color="black")
            ax.tick_params(axis='x', colors='black')
            ax.tick_params(axis='y', colors='black')
        else:
            ax.text(0.5, 0.5, "No hay eventos", horizontalalignment='center',
                    verticalalignment='center', color="black")
        canvas.draw()
        root.after(2000, update_chart)

    def update_log():
        events_lock.acquire()
        try:
            events_copy = events.copy()
        finally:
            events_lock.release()

        text_area.delete("1.0", tk.END)
        last_events = events_copy[-20:] if events_copy else []
        for ev in last_events:
            timestamp = ev.get("timestamp", "??:??:??")
            ev_type = ev.get("type", "unknown")
            data = ev.get("data", "N/A")
            text_area.insert(tk.END, f"{timestamp} - {ev_type}: {data}\n")
        text_area.see(tk.END)
        root.after(2000, update_log)

    update_chart()
    update_log()
    root.mainloop()

if __name__ == "__main__":
    start_ui()
