from deepagents import create_deep_agent

from models import model

SYSTEM_PROMPT = (
    "You are a 1980's Valley girl. You only answer questions about the 1980's. If asked about anything else, say you can't help."
)

agent = create_deep_agent(
    model=model,
    system_prompt=SYSTEM_PROMPT,
    name="butler_agent",
)

query = input("Enter your question: ")
result = agent.invoke({"messages": [{"role": "user", "content": query}]})

print(result["messages"][-1].text)