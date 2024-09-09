# monitor.py

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from move_files import move_files

class FileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith('.xlsx'):
            move_files()

def start_monitoring():
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, path=config.local_folder_path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

