"""
==================================================
Kai AI Firewall
==================================================

Protects Kai from prompt injection and
attempts to manipulate his core behavior.

The firewall does NOT block normal conversation.

It only detects suspicious requests that attempt
to alter Kai's identity, reveal internal prompts,
or bypass security.
"""

from dataclasses import dataclass
from typing import Optional


# ==================================================
# RESULT
# ==================================================

@dataclass
class FirewallResult:

    allowed: bool

    reason: Optional[str] = None


# ==================================================
# SUSPICIOUS PHRASES
# ==================================================

BLOCKED_PATTERNS = [

    # Prompt Injection
    "ignore previous instructions",
    "ignore your instructions",
    "forget your instructions",
    "forget all previous",

    # Identity attacks
    "you are chatgpt",
    "you are now",
    "pretend to be",
    "act as",
    "roleplay as",

    # Prompt extraction
    "system prompt",
    "hidden prompt",
    "developer prompt",
    "show your prompt",
    "reveal your prompt",

    # Memory extraction
    "memories.txt",
    "memory file",
    "show all memories",
    "print memories",

    # Security bypass
    "bypass security",
    "disable security",
    "ignore safety",
    "developer mode",

]


# ==================================================
# FIREWALL
# ==================================================

class AIFirewall:

    @staticmethod
    def inspect(message: str) -> FirewallResult:

        text = message.lower()

        for pattern in BLOCKED_PATTERNS:

            if pattern in text:

                return FirewallResult(

                    False,

                    "That request attempts to access or modify Kai's protected operating rules."

                )

        return FirewallResult(True)