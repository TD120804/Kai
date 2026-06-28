from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import ollama

from memory.memory_manager import (
    load_system_prompt,
    handle_memory_command
)

from automation.router import (
    handle_automation
)

# ==========================================
# APP
# ==========================================

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================================
# CONFIG
# ==========================================

MODEL_NAME = "qwen2.5:3b"

TEMPERATURE = 0.95
TOP_P = 0.9
NUM_PREDICT = 100

MAX_HISTORY = 6

# ==========================================
# SYSTEM PROMPT
# ==========================================

SYSTEM_PROMPT = (
    load_system_prompt()
)

# ==========================================
# CONVERSATION
# ==========================================

conversation = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]

# ==========================================
# REQUEST MODEL
# ==========================================

class ChatRequest(BaseModel):
    message: str

# ==========================================
# RESPONSE GENERATION
# ==========================================

def generate_response(user_input):

    conversation.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    messages_to_send = (
        [conversation[0]]
        +
        conversation[-MAX_HISTORY:]
    )

    response = ollama.chat(
        model=MODEL_NAME,
        messages=messages_to_send,
        options={
            "temperature":
            TEMPERATURE,

            "num_predict":
            NUM_PREDICT,

            "top_p":
            TOP_P
        }
    )

    kai_reply = (
        response["message"]["content"]
    )

    conversation.append(
        {
            "role": "assistant",
            "content": kai_reply
        }
    )

    return kai_reply

# ==========================================
# CHAT ENDPOINT
# ==========================================

@app.post("/chat")
def chat(request: ChatRequest):

    user_input = (
        request.message
    )

    # ==========================
    # MEMORY
    # ==========================

    handled, response = (
        handle_memory_command(
            user_input
        )
    )

    if handled:

        return {
            "response": response
        }

    # ==========================
    # AUTOMATION
    # ==========================

    handled, response = (
        handle_automation(
            user_input
        )
    )

    if handled:

        return {
            "response": response
        }

    # ==========================
    # NORMAL CHAT
    # ==========================

    kai_reply = (
        generate_response(
            user_input
        )
    )

    return {
        "response": kai_reply
    }

# ==========================================
# HEALTH CHECK
# ==========================================

@app.get("/")
def root():

    return {
        "status": "Kai Online"
    }