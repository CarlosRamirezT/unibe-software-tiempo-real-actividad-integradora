import time
from .db_handler import store_event
from .data_capture import events

def process_events():
    while True:
        if events:
            # Se extrae el primer evento de la lista
            event = events.pop(0)
            store_event(event)
        time.sleep(1)
