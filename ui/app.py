import tkinter as tk
from ui_helper import update_status

def main():
    root = tk.Tk()
    root.title("Monitoreo en Tiempo Real de Actividad")
    
    status_label = tk.Label(root, text="Monitorizando actividad...", font=("Arial", 14))
    status_label.pack(pady=20)
    
    # Actualiza la etiqueta con información simulada
    update_status(status_label)
    
    root.mainloop()

if __name__ == "__main__":
    main()
