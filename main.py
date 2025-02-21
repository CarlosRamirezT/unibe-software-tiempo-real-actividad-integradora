import threading
from backend.data_capture import capture_active_app, capture_internet_usage, capture_keyboard, capture_mouse
from backend.data_processor import process_events

def main():
    # Iniciar hilos para la captura de datos
    threading.Thread(target=capture_active_app, daemon=True).start()
    threading.Thread(target=capture_internet_usage, daemon=True).start()
    threading.Thread(target=capture_keyboard, daemon=True).start()
    threading.Thread(target=capture_mouse, daemon=True).start()
    
    # Iniciar hilo para procesar eventos
    threading.Thread(target=process_events, daemon=True).start()
    
    # Mantener el hilo principal activo
    while True:
        pass

if __name__ == "__main__":
    main()
