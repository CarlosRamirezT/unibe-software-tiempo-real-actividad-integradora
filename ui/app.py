import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# IMPORTANTE: importa la lista de eventos del backend
# (Asegúrate de que 'events' sea una variable global en data_capture.py)
from backend.data_capture import events

def start_ui():
    root = tk.Tk()
    root.title("Monitoreo en Tiempo Real de Actividad")
    root.geometry("800x600")
    root.configure(bg="white")  # Fuerza fondo blanco en la ventana principal

    # Frame para el gráfico (parte superior), con fondo blanco
    chart_frame = tk.Frame(root, bg="white")
    chart_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=False)

    # Frame para el log (parte inferior), con fondo blanco
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
        """
        Agrupa los eventos por 'type' para mostrar un gráfico de barras
        con el total de cada tipo de evento.
        """
        # Construir un diccionario con los totales
        totals = {}
        for ev in events:
            ev_type = ev.get("type", "unknown")
            totals[ev_type] = totals.get(ev_type, 0) + 1

        # Limpiar el eje y dibujar el gráfico de barras
        ax.clear()
        if totals:
            labels = list(totals.keys())
            values = list(totals.values())
            ax.bar(labels, values, color='skyblue')
            ax.set_title("Totales de Eventos por Tipo (Tiempo Real)", color="black")
            ax.set_ylabel("Cantidad", color="black")
            # Ajustar color de ejes y ticks
            ax.tick_params(axis='x', colors='black')
            ax.tick_params(axis='y', colors='black')
        else:
            # Si no hay eventos, mostramos un mensaje en el gráfico
            ax.text(0.5, 0.5, "No hay eventos aún", horizontalalignment='center',
                    verticalalignment='center', color="black")
        canvas.draw()

        # Actualizar el gráfico cada 2 segundos
        root.after(2000, update_chart)

    def update_log():
        """
        Muestra los últimos 20 eventos en el área de texto.
        """
        text_area.delete("1.0", tk.END)
        last_events = events[-20:] if events else []
        for ev in last_events:
            # Formatear el evento para mostrarlo
            timestamp = ev.get("timestamp", "??:??:??")
            ev_type = ev.get("type", "unknown")
            data = ev.get("data", "N/A")
            text_area.insert(tk.END, f"{timestamp} - {ev_type}: {data}\n")
        text_area.see(tk.END)

        # Actualizar el log cada 2 segundos
        root.after(2000, update_log)

    # Iniciar las actualizaciones periódicas
    update_chart()
    update_log()

    root.mainloop()

if __name__ == "__main__":
    start_ui()
