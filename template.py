import os
from pathlib import Path
import logging

logging.basicConfig(level= logging.INFO, format= '[%(asctime)s]: %(message)s:')
project_name = "JiaDau_finance_chatbot"

list_of_file = [
    "src/backend/main.py",
    "src/backend/api/chat.py",
    "src/backend/services/llm_service.py",
    "src/backend/services/financial_engine.py",
    "src/backend/services/state_machine.py",
    "src/backend/models/schema.py",
    "src/backend/db/memory.py",
    "requirements.txt"
]

for filepath in list_of_file:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for this file {filename}")

    if (not os.path.exists(filepath) or (os.path.getsize(filepath) == 0)):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filename}")
    else:
        logging.info(f"{filename} is already created")