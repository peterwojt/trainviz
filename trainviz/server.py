import threading
import uvicorn

_started = False

#TODO: make host and port configurable
def _run():
    uvicorn.run(
        "trainviz.app:app",
        host="127.0.0.1",
        port=8000,
        log_level="warning",
    )

def start():
    """
    Launch the Trainviz server.
    """
    global _started
    if _started:
        return
    thread = threading.Thread(target=_run, daemon=True)
    thread.start()
    _started = True
    print("Trainviz started\nView training progress at http://localhost:8000")
