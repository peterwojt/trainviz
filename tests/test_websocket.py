import asyncio
import json
import websockets
import trainlytics as tl

tl.start()

async def ws_test():
    uri = "ws://127.0.0.1:8000/ws"
    async with websockets.connect(uri) as ws:
        tl.update_value("accuracy", 0.99)
        await asyncio.sleep(0.1)
        msg = await ws.recv()
        data = json.loads(msg)
        assert data["accuracy"] == 0.99

def test_websocket_update():
    asyncio.run(ws_test())
