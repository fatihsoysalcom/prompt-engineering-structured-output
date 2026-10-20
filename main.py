import json

def simulate_llm_response(prompt: str, input_text: str) -> str:
    """
    Simulates an LLM response based on the prompt's structure.
    This function demonstrates how different prompts can lead to
    unstructured vs. structured outputs, mimicking the article's concept
    of "deceiving tricks" (unstructured) and "real solutions" (structured).
    """
    # Check for keywords indicating a request for structured JSON output
    if "JSON" in prompt.upper() and ("author" in prompt.lower() or "title" in prompt.lower() or "year" in prompt.lower()):
        # Simulate a structured JSON response based on the input_text
        # In a real LLM, this would involve actual parsing of input_text
        # For this simulation, we'll extract simple values from the example text
        author = "N/A"
        title = "N/A"
        year = "N/A"

        # Simple simulated extraction based on keywords in input_text
        if "Author:" in input_text:
            author = input_text.split("Author:")[1].split('\n')[0].strip()
        if "Title:" in input_text:
            title = input_text.split("Title:")[1].split('\n')[0].strip()
        if "Publication Year:" in input_text:
            year = input_text.split("Publication Year:")[1].split('\n')[0].strip()

        return json.dumps({"author": author, "title": title, "year": year}, indent=2)
    # Check for keywords indicating a request for an unstructured summary
    elif "summarize" in prompt.lower() or "main points" in prompt.lower():
        # Simulate an unstructured, conversational summary
        return (
            "This document discusses the importance of effective communication with AI models. "
            "It highlights that clear and structured prompts are crucial for obtaining "
            "predictable and useful results from large language models. "
            "The author emphasizes that poorly defined prompts can lead to "
            "misinterpretations and unexpected outputs, which is the 'deceiving trick' mentioned."
        )
    else:
        return "I couldn't understand your request clearly. Please be more specific."

# --- Example Usage --- 

document_text = """
Title: The Art of Prompting: A Guide to Effective AI Communication
Author: Jane Doe
Publication Year: 2023
Abstract: This paper explores the nuances of prompt engineering,
emphasizing its critical role in harnessing the full potential of
large language models. It details common pitfalls and offers
strategies for crafting prompts that yield precise and desired outcomes.
"""

print("--- Scenario 1: Vague Prompt (The 'Deceiving Trick') ---")
# This prompt is vague and doesn't specify an output format.
# It's analogous to the "5 times deceiving trick" because the output
# is unstructured and difficult to process programmatically.
vague_prompt = "Summarize this document and tell me the main points."
print(f"Prompt: {vague_prompt}")
vague_response = simulate_llm_response(vague_prompt, document_text)
print(f"LLM Response:\n{vague_response}\n")

# Attempting to programmatically extract info from vague response (difficult)
print("Attempting to parse vague response programmatically (difficult):")
if "Jane Doe" in vague_response:
    print("Found 'Jane Doe' (but it's just a string search, not structured data). This is unreliable.")
else:
    print("Could not reliably extract structured data.")
print("-" * 50 + "\n")


print("--- Scenario 2: Engineered Prompt (The 'Real Solution') ---")
# This prompt is engineered to explicitly request a structured output (JSON).
# This is the "code-based solution" that makes outputs predictable and parsable.
engineered_prompt = f"""
From the following document, extract the 'Author', 'Title', and 'Publication Year'.
Return the information as a JSON object with keys 'author', 'title', and 'year'.

Document:
{document_text}
"""

print(f"Prompt:\n{engineered_prompt}")
structured_response = simulate_llm_response(engineered_prompt, document_text)
print(f"LLM Response:\n{structured_response}\n")

# Programmatically extracting info from structured response (easy)
print("Attempting to parse structured response programmatically (easy):")
try:
    data = json.loads(structured_response)
    print(f"Author: {data.get('author')}")
    print(f"Title: {data.get('title')}")
    print(f"Year: {data.get('year')}")
except json.JSONDecodeError:
    print("Failed to decode JSON. The prompt engineering was not successful, or LLM didn't follow instructions.")
