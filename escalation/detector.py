import logging

logger = logging.getLogger(__name__)

HUMAN_REQUEST_PHRASES = [
    "talk to a human",
    "speak to a person",
    "real person",
    "speak to manager",
    "human agent",
    "customer service representative",
    "talk to someone",
    "speak to a human",
    "real agent",
    "talk to a manager",
    "speak with a manager",
    "speak with a human",
    "connect me to a human",
    "transfer to agent",
]


def should_escalate(message: str, classification: dict) -> dict:
    """Determine whether a customer message should be escalated to a human agent.

    Escalates ONLY when the customer explicitly asks for a human agent.
    Low confidence and negative sentiment do not auto-escalate.

    Args:
        message: The customer's message text.
        classification: Unused in manual-escalation-only mode.

    Returns:
        A dict with ``should_escalate`` (bool), ``reason`` (str), and
        ``details`` (str).
    """
    message_lower = message.lower()

    # Check 1: Explicit human request
    for phrase in HUMAN_REQUEST_PHRASES:
        if phrase in message_lower:
            logger.info(
                "Escalation triggered: human request phrase '%s' in message: %s",
                phrase,
                message[:80],
            )
            return {
                "should_escalate": True,
                "reason": "customer_request",
                "details": f"Customer explicitly requested a human agent: '{phrase}'.",
            }

    return {
        "should_escalate": False,
        "reason": "",
        "details": "",
    }
