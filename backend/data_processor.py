import time
from .db_handler import store_event
from .data_capture import events, events_lock, event_count

def process_events():
    while True:
        # Espera a que exista al menos un evento
        event_count.acquire()
        events_lock.acquire()
        try:
            event = events.pop(0)
        finally:
            events_lock.release()
        store_event(event)
        time.sleep(1)
