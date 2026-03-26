# IMPORTANT: kalibr must be the first import.
# It instruments OpenAI and Anthropic SDK clients at import time.
import kalibr  # noqa: F401 — must be first

import os
from dotenv import load_dotenv
from kalibr import Router

load_dotenv()


def build_agent() -> Router:
    """
    Build the production agent router.

    Replace 'customer_support' with your task name.
    Replace paths with the models you want to route between.
    Define success_when based on what a good output looks like for your task.
    """
    return Router(
        goal="customer_support",              # Your task name — descriptive, stable
        paths=[
            "gpt-4o",                         # Primary path
            "claude-sonnet-4-20250514",        # Fallback — Kalibr routes here when primary degrades
        ],
        success_when=lambda output: (
            output is not None
            and len(output) > 30              # Non-trivial response
            and "error" not in output.lower() # No error strings
        ),
    )


def run_agent(user_message: str) -> str:
    """
    Run the agent on a user message.

    Returns the agent's response. Kalibr handles model selection,
    outcome tracking, and routing — you just call completion().
    """
    router = build_agent()

    response = router.completion(
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful assistant. "
                    "Respond clearly and concisely to the user's request."
                ),
            },
            {
                "role": "user",
                "content": user_message,
            },
        ],
        max_tokens=500,
    )

    # Same interface as OpenAI — response.choices[0].message.content
    return response.choices[0].message.content


def main():
    """Example usage."""
    print("Kalibr Agent Starter
")

    test_messages = [
        "How do I reset my password?",
        "What are your business hours?",
        "I need help with my order.",
    ]

    for msg in test_messages:
        print(f"User: {msg}")
        response = run_agent(msg)
        print(f"Agent: {response}
")


if __name__ == "__main__":
    main()
