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

def update_value(key: str, value, sample_rate=1, sliding_window=None):
    """
    Update a tracked metric.

    Parameters
    ----------
    key : str
        Name of the metric (e.g. "loss", "accuracy").
    value : float
        New value to record.
    sample_rate : int, optional
        Aggregate every N values before storing.
    window : int, optional
        Sliding window size to keep in memory.
    """
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
