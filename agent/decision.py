def agent_decision(query):
    q = query.lower()

    if "weather" in q or "temperature" in q:
        return "api"

    elif "today" in q or "latest" in q:
        return "hybrid"

    else:
        return "rag"
