import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from backend.data_capture import events

def start_ui():
    # Configuración de la ventana principal
    root = tk.Tk()
    root.title("Monitoreo en Tiempo Real de Actividad")
    root.geometry("800x600")
    
    # Frame para el gráfico (parte superior)
    chart_frame = tk.Frame(root)
    chart_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=False)
    
    # Frame para el log (parte inferior)
    log_frame = tk.Frame(root)
    log_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
    
    # Crear la figura y eje para el gráfico
    fig, ax = plt.subplots(figsize=(8, 3))
    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    
    # Crear el widget de texto para el log
    text_area = ScrolledText(log_frame, wrap=tk.WORD, width=100, height=20)
    text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    
    def update_chart():
        """Actualiza el gráfico mostrando el total de eventos por tipo."""
        # Agrupar eventos por 'type'
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
            ax.set_title("Totales de Eventos por Tipo")
            ax.set_ylabel("Cantidad")
        else:
            ax.text(0.5, 0.5, "No hay eventos", horizontalalignment='center', verticalalignment='center')
        canvas.draw()
        root.after(2000, update_chart)  # Actualizar cada 2 segundos
    
    def update_log():
        """Actualiza el log mostrando los últimos eventos capturados."""
        text_area.delete("1.0", tk.END)
        # Mostrar los últimos 20 eventos
        last_events = events[-20:] if events else []
        for ev in last_events:
            text_area.insert(tk.END, f"{ev['timestamp']} - {ev['type']}: {ev['data']}\n")
        text_area.see(tk.END)
        root.after(2000, update_log)
    
    # Iniciar las actualizaciones periódicas
    update_chart()
    update_log()
    
    # Iniciar la interfaz gráfica
    root.mainloop()

if __name__ == "__main__":
    start_ui()
