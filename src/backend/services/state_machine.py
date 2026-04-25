from services.llm_service import *
from db.memory import memory_store

REQUIRED_FIELDS = ["name", "income", "emergency_fund"]

async def handle_massage(user_id, message):
    user_data = memory_store[user_id]
    profile = user_data["profile"]
    user_data["history"].append({"role": "user", "content": message})

    extracted = extract_info(message)
    for k, v in extracted.items():
        if v is not None:
            profile[k] = v

    for field in REQUIRED_FIELDS:
        if profile[field] is None:
            answer = await generation_question(field)
            user_data["history"].append({"role": "assistant", "content": answer})
            return answer
    return f"Ok 👍 thu nhập của {profile['name']} là {profile['income']} và quỹ dự phòng: {profile['emergency_fund']}"