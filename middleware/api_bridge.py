from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


from security.pipeline import (
    SecurityPipeline
)

from brain.conversation import (
    generate_response
)

from memory.memory_manager import (
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
# REQUEST MODEL
# ==========================================

class ChatRequest(BaseModel):

    message: str


# ==========================================
# CHAT
# ==========================================

@app.post("/chat")
def chat(request: ChatRequest):

    user_input = (
        request.message
    )

    # ======================================
    # SECURITY PIPELINE
    # ======================================

    security = (
        SecurityPipeline.process(
            user_input
        )
    )

    if not security.success:

        return {
            "response": security.error
        }

    user_input = (
        security.message
    )

    # ======================================
    # MEMORY
    # ======================================

    handled, response = (
        handle_memory_command(
            user_input
        )
    )

    if handled:

        return {
            "response": response
        }

    # ======================================
    # AUTOMATION
    # ======================================

    handled, response = (
        handle_automation(
            user_input
        )
    )

    if handled:

        return {
            "response": response
        }

    # ======================================
    # NORMAL CHAT
    # ======================================

    return {
        "response":
        generate_response(
            user_input
        )
    }

    # ======================================
    # MEMORY
    # ======================================

    handled, response = (
        handle_memory_command(
            user_input
        )
    )

    if handled:

        return {
            "response": response
        }

    # ======================================
    # AUTOMATION
    # ======================================

    handled, response = (
        handle_automation(
            user_input
        )
    )

    if handled:

        return {
            "response": response
        }

    # ======================================
    # NORMAL CHAT
    # ======================================

    return {
        "response":
        generate_response(
            user_input
        )
    }


# ==========================================
# ROOT
# ==========================================

@app.get("/")
def root():

    return {

        "status": "online",

        "assistant": "Kai",

        "version": "0.1.0"

    }


# ==========================================
# STATUS
# ==========================================

@app.get("/status")
def status():

    return {

        "online": True,

        "assistant": "Kai",

        "model": "qwen2.5:3b",

        "memory": True,

        "automation": True,

        "api": True

    }