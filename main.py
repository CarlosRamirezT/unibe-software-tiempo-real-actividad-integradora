import threading
from backend.main import start_backend as backend_init
from ui.app import start_ui as frontend_init

def main():
    # Iniciar los hilos del backend en segundo plano.
    backend_init()

    # Iniciar la interfaz gráfica (Tkinter) en el hilo principal.
    frontend_init()

if __name__ == "__main__":
    main()
