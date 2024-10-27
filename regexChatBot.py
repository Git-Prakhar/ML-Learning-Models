import re

patternResponse = {
    r'^(hi|hello|hey)':"Hello! I am a Simple Chat Bot Created using Regular Expressions",
    r'how are you':"I am Good! How are you?",
    r'i am (good|fine|happy)':"Thats Great!",
    r'i am (sad|bad)':"Oh! I see",
    r'exit|quit': "See ya later aligator",
    r'.*':"What?"
}

def response(message):
    for pattern, res in patternResponse.items():
        match = re.search(pattern, message, re.IGNORECASE)
        if match:
            return res
    return 'What?'

def chatBot():
    print('Bot: Hello there!')
    while True:
        message = input()
        res = response(message)
        print("Bot :", res)
        if re.search('exit|quit', message, re.IGNORECASE):
            break

chatBot()