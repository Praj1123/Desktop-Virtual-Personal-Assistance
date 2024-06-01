from hugchat import hugchat
def chatBot(query):
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path="Luna\cookies.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response =  chatbot.chat(user_input)
    print(response)
    return response

chatBot('Hey how are you')