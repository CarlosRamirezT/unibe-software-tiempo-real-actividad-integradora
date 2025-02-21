import threading
from .data_capture import capture_active_app, capture_internet_usage, capture_keyboard, capture_mouse
from .data_processor import process_events

def start_backend():
    # Inicia los hilos del backend en modo daemon para que no bloqueen el hilo principal
    threading.Thread(target=capture_active_app, daemon=True).start()
    threading.Thread(target=capture_internet_usage, daemon=True).start()
    threading.Thread(target=capture_keyboard, daemon=True).start()
    threading.Thread(target=capture_mouse, daemon=True).start()
    threading.Thread(target=process_events, daemon=True).start()

if __name__ == "__main__":
    start_backend()
    import time
    while True:
        time.sleep(1)
