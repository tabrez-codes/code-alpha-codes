import nltk
from nltk.chat.util import Chat, reflections
nltk.download('punkt')
pairs = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey, how can I help you?']),
    (r'how are you?', ['I am doing great, thank you for asking!', 'I am good, how about you?']),
    (r'what is your name?', ['I am a chatbot created using nltk. You can call me Bot.']),
    (r'quit', ['Goodbye! Have a nice day!']),
    (r'(.*)', ['Sorry, I did not understand that. Can you please rephrase?']),
]
chatbot = Chat(pairs, reflections)
def chatbot_conversation():
    print("Hello! I am your chatbot. Type 'quit' to end the conversation.")
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("Bot: " + response)
        if user_input.lower() == 'quit':
            break
chatbot_conversation()
