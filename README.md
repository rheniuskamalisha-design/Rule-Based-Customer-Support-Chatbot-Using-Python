# Rule-Based Customer Support Chatbot

A beginner-friendly Python customer support chatbot that uses regular expressions,
keyword matching and a JSON FAQ dataset.

## Project files

- `chatbot.py` - Main chatbot program.
- `faq.json` - Questions/keywords and their responses.
- `README.md` - Setup and usage instructions.

## Requirements

- Python 3.8 or later
- Visual Studio Code (recommended)
- No third-party Python packages are required. The program uses Python's
  built-in `re`, `json` and `pathlib` modules.

## Run in VS Code

1. Extract the ZIP file.
2. Open the extracted `Customer_Support_Chatbot` folder in VS Code.
3. Open **Terminal > New Terminal**.
4. Run:

   ```bash
   python chatbot.py
   ```

   On some Windows installations, use:

   ```bash
   py chatbot.py
   ```

## Example questions

- Hi
- What are your business hours?
- What is the product price?
- Tell me the product features
- Do you provide warranty?
- How long does delivery take?
- How can I track my order?
- How can I contact support?
- bye

## Customize the FAQ

Open `faq.json`. Each FAQ entry contains:
- `keywords`: phrases that help the chatbot recognize the question.
- `response`: the answer shown to the user.

You can add more FAQ entries using the same JSON structure.

## Notes

The business information and product details in this sample are placeholders.
Replace them with the real details of your organization before presenting or deploying
the chatbot.
