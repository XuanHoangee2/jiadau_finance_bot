from fastapi import WebSocket, FastAPI
import uuid
from db.memory import memory_store
from services.state_machine import handle_massage


app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(ws:WebSocket):
    await ws.accept()

    user_id = str(uuid.uuid4())
    memory_store[user_id] = {
        "profile": {
        "name": None,
        "income": None,
        "emergency_fund": None
        },
        "history": []
    }
    await ws.send_text("Chào bạn 👋 Tôi sẽ giúp bạn kiểm tra tài chính.")
    while True:
        data = await ws.receive_text()
        response = await handle_massage(user_id, data)
        await ws.send_text(response) 