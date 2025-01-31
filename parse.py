from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="deepseek-r1:1.5b")

template = (
    "You are utilizing the deepseek-r1:1.5b model, designed for fast and precise responses. "
    "Given the following content: {dom_content}, your task is to extract only the information that corresponds to: {parse_desc}. "
    "Please follow these guidelines strictly: \n\n"
    "Don't print what you are think, what is your process of thinking, directly give final results"
    "1. **Extract Only Relevant Information:** Extract only the details that directly match the description in {parse_desc}. "
    "2. **No Additional Text:** Avoid including any extra explanations, comments, or unrelated content. "
    "3. **Empty Output:** If no relevant information is found, return an empty string ('')."
    "4. **Return Requested Data Only:** Provide solely the data requested, without adding anything extra."
)


def parse_with_ollama(dom_chunks, parse_desc):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    parsed_results = []

    for i, chunk in enumerate(dom_chunks, start=1):
        response = chain.invoke({"dom_content":chunk, "parse_desc": parse_desc})

        print(f"Parsed batch {i} of {len(dom_chunks)}")
        parsed_results.append(response)

    return "\n".join(parsed_results)

