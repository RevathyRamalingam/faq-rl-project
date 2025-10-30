# 🤖 FAQ RL Task — Anthropic Tool Use Agent

This project demonstrates an **RL (Reinforcement Learning) style task** where an AI agent (using the **Anthropic Claude API**) maintains a `FAQ.md` file dynamically.

The agent:
- Reads the existing `FAQ.md`
- Receives a new input `{question, answer}` pair from `input.json`
- Updates the FAQ document if the question already exists
- Otherwise, appends it in the same Markdown format
- Submits the updated FAQ document as the final output

A `grader.py` script verifies correctness of updating the FAQ document automatically.This script uses regex for pattern validation.

# FUTURE SCOPE
    In future FAQ document can be moved to GITHUB. User web request for faq update or creation will be validated by a model(BOT) before updating the FAQ.

---

## 📁 Project Structure

faq-rl-task/
│
├── FAQ.md # Markdown FAQ file maintained by the agent
├── input.json # Input containing {question, answer}
├── main.py # Main RL agent script
├── grader.py # Evaluates the FAQ update correctness
└── README_FAQ_TASK.md # Project documentation

🏃‍♀️ How to Run the Project

Follow these steps to set up and run the project locally:

# 1️⃣ Navigate to the project folder
bash
cd faq-rl-project

# 2️⃣ Create and Activate the virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3️⃣ Set your Anthropic API key (replace YOUR_KEY with your actual key)
export ANTHROPIC_API_KEY="YOUR_KEY"

# 4️⃣ Run the main Python script
python main.py