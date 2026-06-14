# Kai Bug Log

## Duplicate System Prompt Bug

Issue:
Kai suddenly became extremely slow.

Symptoms:
- 45+ second responses

Cause:
System prompt was being sent twice.

Fix:
Removed duplicate system prompt from messages_to_send.

Result:
Latency reduced to ~2.4 seconds.