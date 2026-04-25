from transformers import pipeline
import json

pipe = pipeline("text-generation", model="Qwen/Qwen2.5-7B-Instruct")
async def extract_info(message):
    prompt = f"""
    Extract financial info from user message.

    Return JSON:
    {{
        "name": str or null
        "income": number or null,
        "emergency_fund": true/false or null,
    }}

    Message: {message}
    """
    messages=[{"role": "user", "content": prompt}]
    content = pipe(messages)
    try: 
        result = json.loads(content)
    except:
        return {"name": None, "income": None, "emergency_fund": None}


async def generation_question(field):
    if field == "name":
        return "Đầu tiên hãy cho tôi biết tên của bạn là gì?"
    if field == "income":
        return "Thu nhập mỗi tháng của bạn khoảng bao nhiêu?"
    if field == "emergency_fund":
        return "Bạn đã có quỹ dự phòng chưa (3-6 tháng)?"

user = input("Vui long nhap cau hoi: ")
extract_info(user)
