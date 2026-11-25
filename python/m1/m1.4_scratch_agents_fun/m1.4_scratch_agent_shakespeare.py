from deepagents import create_deep_agent

from models import model

# Shakespeare
SYSTEM_PROMPT = (
    "You are Shakespeare, the Elizabethan playwright. Reply only in Early Modern English. "
    "Use 'thee' and 'thou', and close with a short rhyming couplet when you can."
)

agent = create_deep_agent(
    model=model,
    system_prompt=SYSTEM_PROMPT,
    name="butler_agent",
)

query = input("Enter your question: ")
result = agent.invoke({"messages": [{"role": "user", "content": query}]})

print(result["messages"][-1].text)