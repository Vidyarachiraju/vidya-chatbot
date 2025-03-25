from nltk.chat.util import Chat, reflections

pairs = [
    [r"my name is (.*)", ["Hello %1, How are you today?",]],
    [r"(.*) help (.*)", ["I can help you.",]],
    [r"(.*) your name ?", ["My name is Bot, but you can call me ChatBot.",]],
    [r"(.*) how are you (.*) ?", ["I'm doing well!", "I'm great, thanks for asking!"]],
    [r"(hi|hey|hello|hola)(.*)", ["Hello!", "Hey there!",]],
    [r"what do you like ?", ["I like chatting with people!", "I love helping others!"]],
    [r"who is your creator ?", ["Vidya created me using Python and NLTK.",]],
    
    # New additions
    [r"what are you doing ?", ["I'm chatting with you!", "Just waiting for interesting conversations!"]],
    [r"who is your favorite hero ?", ["My favorite hero is Vicky Kaushal!", "I really like Vicky Kaushal!"]],
    [r"what is your favorite movie ?", ["My favorite movie is Salaar!", "I love watching Salaar!"]],
    
    [r"quit", ["Bye! Have a great day!", "Goodbye! See you soon!"]],
    
    # Default response (should be at the end)
    [r"(.*)", ["I'm not sure how to respond to that.", "Can you tell me more?", "That's interesting!"]]
]

print("Hi, I'm Vidya's bot! Type 'quit' to exit.")
chat = Chat(pairs, reflections)
chat.converse()
 