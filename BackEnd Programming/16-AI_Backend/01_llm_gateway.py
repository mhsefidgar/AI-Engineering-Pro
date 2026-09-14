"""Provider-neutral LLM gateway lab.

The point is to keep HTTP/API code independent from a specific model SDK.
"""
from dataclasses import dataclass
from typing import Protocol

@dataclass(frozen=True)
class ChatResult:
    text: str
    input_tokens: int
    output_tokens: int
    model: str

class LLMProvider(Protocol):
    async def complete(self, messages: list[dict[str, str]], *, model: str) -> ChatResult: ...

async def run_inference(provider: LLMProvider, messages: list[dict[str, str]], model: str) -> ChatResult:
    if not messages:
        raise ValueError("messages must not be empty")
    if len(messages) > 100:
        raise ValueError("too many messages")
    return await provider.complete(messages, model=model)

# Exercises:
# 1. Implement a real provider adapter behind LLMProvider.
# 2. Add timeout and bounded retry behavior.
# 3. Add a second provider and fallback routing.
# 4. Record latency, token usage, model, and estimated cost.
# 5. Add per-user rate limits and budgets.
# 6. Add streaming without leaking provider-specific response types.
# 7. Add prompt/version metadata for reproducibility.
# 8. Add tests for provider timeout, malformed output, and fallback failure.
