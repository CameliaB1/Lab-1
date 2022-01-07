from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

my_bot = ChatBot(
    'Kevin', 
    read_only = True,
    storage_adapter = 'chatterbot.storage.SQLStorageAdapter',
    logic_adapters = [
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.MathematicalEvaluation'],
    database_uri = 'sqlite:///database.db')

l_convo = ListTrainer(my_bot)
trainer = ChatterBotCorpusTrainer(my_bot)

l_convo.train([
    'Hi', 
    'Hello', 
    'How is your day?', 
    'Good, yours?',
    'How are you',
    'Good', 
])
    
name = input('Enter your name please: ')
print("Welcome", name, 'to Kevins Service!')
while True:
    request = input(name + ': ')
    if request == "Bye" or request == 'bye':
        print('Kevin: Have a good day!')
        break
    else:
        response = my_bot.get_response(request)
        print('Kevin: ', response)