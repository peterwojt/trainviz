import asyncio
from threading import Lock

class AppState:
    def __init__(self):
        self.data = {}
        self.connections = set()
        self.lock = Lock()

    async def broadcast(self):
        dead = set()
        for ws in self.connections:
            try:
                await ws.send_json(self.data)
            except:
                dead.add(ws)
        self.connections -= dead

STATE = AppState()

def update_value(key, value):
    with STATE.lock:
        STATE.data[key] = value
    try:
        loop = asyncio.get_running_loop()
        loop.create_task(STATE.broadcast())
    except RuntimeError:
        asyncio.run(STATE.broadcast())
