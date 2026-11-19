import re
import json
from pathlib import Path


FAQ_FILE = Path(__file__).with_name("faq.json")


def load_faq():
    """Load the FAQ data from the JSON file."""
    try:
        with FAQ_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as error:
        print(f"Could not load FAQ data: {error}")
        return {}


def normalize_input(user_input):
    """Convert input to lowercase and remove extra whitespace."""
    return re.sub(r"\s+", " ", user_input.lower().strip())


def identify_intent(user_input, faq_data):
    """Identify the user's intent using greetings and FAQ keywords."""
    normalized = normalize_input(user_input)

    if re.search(r"\b(hi|hello|hey|good morning|good afternoon|good evening)\b", normalized):
        return "greeting"

    for intent, data in faq_data.items():
        for keyword in data.get("keywords", []):
            pattern = r"\b" + re.escape(keyword.lower()) + r"\b"
            if re.search(pattern, normalized):
                return intent

    return "unknown"


def generate_response(intent, faq_data):
    """Return a response for the identified intent."""
    if intent == "greeting":
        return "Hello! Welcome to Customer Support. How can I help you today?"

    if intent == "unknown":
        return (
            "Sorry, I couldn't understand your question. "
            "Please ask about business hours, product price, features, "
            "warranty, delivery, order status or contact details."
        )

    return faq_data[intent]["response"]


def is_exit_command(user_input):
    """Check whether the user entered a clean exit command."""
    return bool(re.fullmatch(r"(bye|exit|quit)", normalize_input(user_input)))


def chatbot():
    faq_data = load_faq()

    print("=" * 55)
    print("              CUSTOMER SUPPORT CHATBOT")
    print("=" * 55)
    print("Bot: Hello! Welcome to our Customer Support.")
    print("Bot: Ask me about products, orders or business hours.")
    print("Bot: Type 'bye', 'exit' or 'quit' to close the chatbot.")

    # Simple conversational state: active -> exit
    state = "active"

    while state == "active":
        try:
            user_input = input("\nYou: ")
        except (EOFError, KeyboardInterrupt):
            print("\nBot: Thank you for contacting us. Goodbye!")
            break

        if not user_input.strip():
            print("Bot: Please enter a question so I can help you.")
            continue

        if is_exit_command(user_input):
            print("Bot: Thank you for contacting us. Have a nice day!")
            state = "exit"
            continue

        intent = identify_intent(user_input, faq_data)
        response = generate_response(intent, faq_data)
        print(f"Bot: {response}")


if __name__ == "__main__":
    chatbot()
