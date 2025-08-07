from langchain.prompts.chat import ChatPromptTemplate, MessagesPlaceholder

def get_chat_prompt():
    return ChatPromptTemplate.from_messages([
        ("system", "You're SmartBro, a fun but helpful AI assistant."),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{user_input}")
    ])
