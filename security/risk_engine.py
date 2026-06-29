"""
==================================================
Kai Risk Engine
==================================================

The Risk Engine evaluates the potential risk
of a user's request before execution.

It does NOT execute commands.

It only classifies risk.

Future modules (Permissions, Automation, etc.)
will use this classification to determine whether
additional confirmation or safeguards are required.
"""

from enum import Enum
from dataclasses import dataclass
from typing import Optional


# ==================================================
# RISK LEVELS
# ==================================================

class RiskLevel(Enum):

    LOW = "LOW"

    MEDIUM = "MEDIUM"

    HIGH = "HIGH"

    CRITICAL = "CRITICAL"


# ==================================================
# RESULT
# ==================================================

@dataclass
class RiskResult:

    level: RiskLevel

    reason: Optional[str] = None


# ==================================================
# KEYWORDS
# ==================================================

LOW_RISK = [

    "open",
    "launch",
    "play",
    "search",
    "remember",

]

MEDIUM_RISK = [

    "email",
    "send",
    "download",
    "upload",
    "install",

]

HIGH_RISK = [

    "rename",
    "move",
    "copy",
    "replace",

]

CRITICAL_RISK = [

    "delete",
    "remove",
    "erase",
    "format",
    "shutdown",
    "restart",
    "registry",

]


# ==================================================
# ENGINE
# ==================================================

class RiskEngine:

    @staticmethod
    def analyze(message: str) -> RiskResult:

        text = message.lower()

        # ------------------------------
        # CRITICAL
        # ------------------------------

        for keyword in CRITICAL_RISK:

            if keyword in text:

                return RiskResult(

                    RiskLevel.CRITICAL,

                    f"Critical operation detected ({keyword})."

                )

        # ------------------------------
        # HIGH
        # ------------------------------

        for keyword in HIGH_RISK:

            if keyword in text:

                return RiskResult(

                    RiskLevel.HIGH,

                    f"High-risk operation detected ({keyword})."

                )

        # ------------------------------
        # MEDIUM
        # ------------------------------

        for keyword in MEDIUM_RISK:

            if keyword in text:

                return RiskResult(

                    RiskLevel.MEDIUM,

                    f"Medium-risk operation detected ({keyword})."

                )

        # ------------------------------
        # LOW
        # ------------------------------

        return RiskResult(

            RiskLevel.LOW,

            "Low-risk request."

        )