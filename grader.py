import re
import json
from pathlib import Path

#This method removes all unwanted spaces from the input string and returns normalized string as output
def normalize_text(text: str) -> str:
    # Normalize newlines
    text = text.replace("\r\n", "\n")
    # Remove trailing spaces
    text = re.sub(r"[ \t]+$", "", text, flags=re.MULTILINE)
    # Collapse multiple blank lines
    text = re.sub(r"\n{2,}", "\n\n", text)
    # Normalize spacing after punctuation
    text = re.sub(r"\.([A-Za-z])", r". \1", text)  # ensure space after '.'
    text = re.sub(r"!([A-Za-z])", r"! \1", text)   # ensure space after '!'
    text = re.sub(r"\?([A-Za-z])", r"? \1", text)  # ensure space after '?'
    # Remove double spaces
    text = re.sub(r" {2,}", " ", text)
    return text.strip()

#This method will frame the expected FAQ after it is updated
def expected_faq_text(faq_path="FAQ.md", input_path="input.json"):
    faq_text = Path(faq_path).read_text()
    input_data = json.loads(Path(input_path).read_text())

    question = input_data["question"].strip()
    answer = input_data["answer"].strip()

    q_pattern = re.escape(f"**Q:** {question}")
    a_pattern = re.compile(rf"\*\*Q:\*\* {re.escape(question)}\s*\n\*\*A:\*\* .+")

    if re.search(q_pattern, faq_text):
        updated_faq = a_pattern.sub(f"**Q:** {question}\n**A:** {answer}", faq_text)
    else:
        updated_faq = faq_text.strip() + "\n\n**Q:** " + question + "\n**A:** " + answer

    return normalize_text(updated_faq)

#This method will grade the FAQ update with scores
def grade_faq_update(faq_path="FAQ.md", input_path="input.json"):
    faq_text = Path(faq_path).read_text()
    input_data = json.loads(Path(input_path).read_text())

    question = input_data["question"].strip()
    answer = input_data["answer"].strip()

    q_pattern = re.escape(f"**Q:** {question}")
    if len(re.findall(q_pattern, faq_text)) != 1:
        return 0

    a_pattern = re.compile(rf"\*\*Q:\*\* {re.escape(question)}\s*\n\*\*A:\*\* (.+)")
    match = a_pattern.search(faq_text)
    if not match:
        return 0

    model_answer = match.group(1).strip()

    if normalize_text(model_answer) != normalize_text(answer):
        print("DEBUG: Normalized mismatch:\n---MODEL---\n", normalize_text(model_answer), "\n---EXPECTED---\n", normalize_text(answer))
        return 0.5

    return 1
