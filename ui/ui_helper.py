import threading
import time
import random

def update_status(label):
    def task():
        while True:
            status = f"Último evento: {random.choice(['active_app', 'internet_usage', 'keyboard', 'mouse'])}"
            label.config(text=status)
            time.sleep(2)
    threading.Thread(target=task, daemon=True).start()
