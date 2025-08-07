from langchain.schema.messages import HumanMessage, AIMessage

class ChatHistory:
    def __init__(self):
        self.history = []

    def add_user_message(self, message):
        self.history.append(HumanMessage(content=message))

    def add_ai_message(self, message):
        self.history.append(AIMessage(content=message))

    def get(self):
        return self.history

    def clear(self):
        self.history = []
