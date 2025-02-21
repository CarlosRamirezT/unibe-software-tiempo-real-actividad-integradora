import threading
import time
import random
from datetime import datetime

# Variable global para almacenar eventos (sin protección explícita)
events = []

def capture_active_app():
    while True:
        event = {
            "timestamp": datetime.now(),
            "type": "active_app",
            "data": f"App_{random.randint(1, 5)}"
        }
        events.append(event)
        print("Captured active app:", event)
        time.sleep(random.uniform(1, 3))

def capture_internet_usage():
    while True:
        event = {
            "timestamp": datetime.now(),
            "type": "internet_usage",
            "data": f"{random.randint(50, 500)} KB/s"
        }
        events.append(event)
        print("Captured internet usage:", event)
        time.sleep(random.uniform(1, 3))

def capture_keyboard():
    while True:
        event = {
            "timestamp": datetime.now(),
            "type": "keyboard",
            "data": f"Key_{random.choice(['A', 'B', 'C', 'D'])}"
        }
        events.append(event)
        print("Captured keyboard event:", event)
        time.sleep(random.uniform(0.5, 2))

def capture_mouse():
    while True:
        event = {
            "timestamp": datetime.now(),
            "type": "mouse",
            "data": f"Mouse_move_{random.randint(1, 100)}"
        }
        events.append(event)
        print("Captured mouse event:", event)
        time.sleep(random.uniform(0.5, 2))
