import asyncio
import json
import time
import requests
import websockets
import trainlytics as tl

tl.start()
time.sleep(0.5)

tl.update_value("loss", 0.42)
tl.update_value("epoch", 3)

# HTTP test
r = requests.get("http://127.0.0.1:8000")
assert r.status_code == 200

# WebSocket test
async def ws_test():
    uri = "ws://127.0.0.1:8000/ws"
    async with websockets.connect(uri) as ws:
        msg = await ws.recv()
        data = json.loads(msg)
        assert data["loss"] == 0.42
        assert data["epoch"] == 3

asyncio.run(ws_test())
