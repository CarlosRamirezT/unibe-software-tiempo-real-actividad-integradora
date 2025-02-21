import time
import random
from datetime import datetime
import threading

# Lista global para almacenar eventos
events = []

# Mutex para acceso exclusivo a 'events'
events_lock = threading.Semaphore(1)

# Semáforo contable para indicar la cantidad de eventos disponibles
event_count = threading.Semaphore(0)

def capture_active_app():
    while True:
        event = {
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "type": "active_app",
            "data": f"App_{random.randint(1, 5)}"
        }
        events_lock.acquire()
        events.append(event)
        events_lock.release()
        event_count.release()  # Indica que se agregó un evento
        print("Captured active app:", event)
        time.sleep(random.uniform(1, 3))

def capture_internet_usage():
    while True:
        event = {
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "type": "internet_usage",
            "data": f"{random.randint(50, 500)} KB/s"
        }
        events_lock.acquire()
        events.append(event)
        events_lock.release()
        event_count.release()
        print("Captured internet usage:", event)
        time.sleep(random.uniform(1, 3))

def capture_keyboard():
    while True:
        event = {
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "type": "keyboard",
            "data": f"Key_{random.choice(['A', 'B', 'C', 'D'])}"
        }
        events_lock.acquire()
        events.append(event)
        events_lock.release()
        event_count.release()
        print("Captured keyboard event:", event)
        time.sleep(random.uniform(0.5, 2))

def capture_mouse():
    while True:
        event = {
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "type": "mouse",
            "data": f"Mouse_move_{random.randint(1, 100)}"
        }
        events_lock.acquire()
        events.append(event)
        events_lock.release()
        event_count.release()
        print("Captured mouse event:", event)
        time.sleep(random.uniform(0.5, 2))
