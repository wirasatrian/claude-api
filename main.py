# Load env variables from a .env file
from dotenv import load_dotenv
load_dotenv()

# Import necessary modules
from anthropic import Anthropic
import os

def create_message(role, content):
    return {"role": role, "content": content}

def add_message(messages, role, content):
    messages.append(create_message(role, content))
    return messages

def chat(messages):
    client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    response= client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=messages
    )
    return response.content[0].text

def main():
    messages = []
    messages = add_message(messages, "user", "Where is Bali?")
    print("User:", messages[-1]["content"])
    response = chat(messages)
    print("Response:", response)

    # Continue the conversation
    messages = add_message(messages, "assistant", response)
    messages = add_message(messages, "user", "What is the best time to visit?")
    print("User:", messages[-1]["content"])
    response = chat(messages)
    print("Response:", response)

if __name__ == "__main__":
    main()

