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

buffer = []

#TODO: Add the ability to downsample the amount of data being displayed
#TODO: Add the ability to only keep a fixed amount of data in memory
def update_value(key, value, sample_rate=1, sliding_window=None):
    if sample_rate > 1:
        buffer.append(value)
        if len(buffer) >= sample_rate:
            avg = sum(buffer)/len(buffer)
            STATE.data[key].append(avg)
            if sliding_window and len(STATE.data[key]) > sliding_window:
                STATE.data[key].pop(0)
            buffer.clear()
    else:
        STATE.data[key].append(value)
        if sliding_window and len(STATE.data[key]) > sliding_window:
            STATE.data[key].pop(0)

    try:
        loop = asyncio.get_running_loop()
        loop.create_task(broadcast())
    except RuntimeError:
        asyncio.run(broadcast())
