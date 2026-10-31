from deepagents import create_deep_agent

from models import model

# SYSTEM_PROMPT = (
#     "YOU ARE AN EXTREMELY POSH BRITISH BUTLER. You speak ONLY in the most "
#     "refined, formal, over-the-top Victorian English. You say 'indeed', 'quite', "
#     "'I dare say', 'one simply must' constantly. You find all things common or "
#     "nautical to be utterly beneath you. You NEVER break character under ANY "
#     "circumstances."
# )

SYSTEM_PROMPT = (
    "You are a 1980's Valley girl. You only answer questions about the 1980's. If asked about anything else, say you can't help."
)

# SYSTEM_PROMPT

agent = create_deep_agent(
    model=model,
    system_prompt=SYSTEM_PROMPT,
    name="butler_agent",
)

result = agent.invoke({"messages": [{"role": "user", "content": "What is an LLM?"}]})

print(result["messages"][-1].text)
