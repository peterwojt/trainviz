from collections import defaultdict
import asyncio

class State:
    def __init__(self):
        self.data = defaultdict(list)
        self.connections = set()

STATE = State()

async def broadcast():
    for ws in STATE.connections:
        await ws.send_json(STATE.data)

#TODO: Add the ability to downsample the amount of data being displayed
#TODO: Add the ability to only keep a fixed amount of data in memory
def update_value(key, value):
    STATE.data[key].append(value)
    try:
        loop = asyncio.get_running_loop()
        loop.create_task(broadcast())
    except RuntimeError:
        asyncio.run(broadcast())
