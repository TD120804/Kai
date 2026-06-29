"""
==================================================
Kai Security Pipeline
==================================================

The Security Pipeline is the single entry point
for all incoming requests.

Every request passes through:

1. Validator
2. Sanitizer
3. AI Firewall
4. Risk Engine
5. Permission Engine

The pipeline returns one unified result.
"""

from dataclasses import dataclass
from typing import Optional

from security.validator import InputValidator
from security.sanitizer import InputSanitizer
from security.firewall import AIFirewall
from security.risk_engine import RiskEngine
from security.permissions import PermissionEngine


# ==================================================
# RESULT
# ==================================================

@dataclass
class SecurityResult:

    success: bool

    message: Optional[str]

    risk: Optional[object]

    permission: Optional[object]

    error: Optional[str] = None


# ==================================================
# PIPELINE
# ==================================================

class SecurityPipeline:

    @staticmethod
    def process(message: str) -> SecurityResult:

        # ------------------------------------------
        # VALIDATOR
        # ------------------------------------------

        validation = (
            InputValidator.validate(message)
        )

        if not validation.valid:

            return SecurityResult(

                False,

                None,

                None,

                None,

                validation.reason

            )

        # ------------------------------------------
        # SANITIZER
        # ------------------------------------------

        message = (
            InputSanitizer.sanitize(message)
        )

        # ------------------------------------------
        # FIREWALL
        # ------------------------------------------

        firewall = (
            AIFirewall.inspect(message)
        )

        if not firewall.allowed:

            return SecurityResult(

                False,

                None,

                None,

                None,

                firewall.reason

            )

        # ------------------------------------------
        # RISK
        # ------------------------------------------

        risk = (
            RiskEngine.analyze(message)
        )

        # ------------------------------------------
        # PERMISSIONS
        # ------------------------------------------

        permission = (
            PermissionEngine.evaluate(risk)
        )

        # ------------------------------------------
        # SUCCESS
        # ------------------------------------------

        return SecurityResult(

            True,

            message,

            risk,

            permission,

            None

        )