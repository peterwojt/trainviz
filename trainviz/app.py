from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from .state import STATE

app = FastAPI(title="Trainviz Dashboard")

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    STATE.connections.add(ws)
    await ws.send_json(STATE.data)
    try:
        while True:
            await ws.receive_text()
    except:
        STATE.connections.remove(ws)

app.mount(
    "/",
    StaticFiles(directory=Path(__file__).parent / "web", html=True),
    name="web",
)
