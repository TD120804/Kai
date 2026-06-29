"""
==================================================
Kai Permission Engine
==================================================

The Permission Engine decides whether Kai
is allowed to execute a request.

It works together with the Risk Engine.

Risk answers:

    "How dangerous is this?"

Permissions answer:

    "Can Kai perform it?"

"""

from enum import Enum
from dataclasses import dataclass
from typing import Optional


# ==================================================
# DECISION
# ==================================================

class PermissionDecision(Enum):

    ALLOW = "ALLOW"

    REQUIRE_CONFIRMATION = "REQUIRE_CONFIRMATION"

    DENY = "DENY"


# ==================================================
# RESULT
# ==================================================

@dataclass
class PermissionResult:

    decision: PermissionDecision

    reason: Optional[str] = None


# ==================================================
# ENGINE
# ==================================================

class PermissionEngine:

    @staticmethod
    def evaluate(risk_result):

        level = risk_result.level.value

        # ------------------------------------------
        # LOW
        # ------------------------------------------

        if level == "LOW":

            return PermissionResult(

                PermissionDecision.ALLOW,

                "Safe to execute."

            )

        # ------------------------------------------
        # MEDIUM
        # ------------------------------------------

        if level == "MEDIUM":

            return PermissionResult(

                PermissionDecision.REQUIRE_CONFIRMATION,

                "Confirmation recommended."

            )

        # ------------------------------------------
        # HIGH
        # ------------------------------------------

        if level == "HIGH":

            return PermissionResult(

                PermissionDecision.REQUIRE_CONFIRMATION,

                "Confirmation required."

            )

        # ------------------------------------------
        # CRITICAL
        # ------------------------------------------

        return PermissionResult(

            PermissionDecision.DENY,

            "Operation blocked until explicitly confirmed."

        )