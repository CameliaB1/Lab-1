from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

my_bot = ChatBot(
    'Kevin', 
    read_only = True,
    storage_adapter = 'chatterbot.storage.SQLStorageAdapter',
    logic_adapters = [
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch', 
            'default_response': 'I am sorry I do not understand. I am still learning'
            }, 
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.MathematicalEvaluation'],
    database_uri = 'sqlite:///database.db')

l_convo = ListTrainer(my_bot)

l_convo.train([ 
    'hello',
    'how is your day',
    'bad',
    'Sorry to here that. What would you like to talk about? I know some classic jokes, a few history facts, and interesting facts.',
])

l_convo.train([
    'hi', 
    'how is your day', 
    'good',
    'What would you like to talk about? I know some classic jokes, a few history facts, and interesting facts.',
])

l_convo.train([ 
    'jokes',
    'Why to melons get married?',
    'why', 
    'They cantalope. Would you like to here another one?',
    'yeah',
    'What do you call a dog magician?',
    'what', 
    'A labracadabrador. Would you like to here another?',
    'no',
    'What else would you like to talk about? I know some classic jokes, a few history facts, and interesting facts.',
])

l_convo.train([
    'history facts', 
    'Paul Revere never shoated "The British are coming!" during the revoultinay war. Would you like to here another?', 
    'yeah', 
    'Napoleon was once attacked by a horde of bunnies. Would you like to here another?',
    'sure', 
    'The owners of the Titanic never acually called in unsinkable. Would you like to here another?',
    'no',
    'What else would you like to talk about? I know some classic jokes, a few history facts, and interesting facts.',
])

l_convo.train([
    'interesting facts',
    'Would you like to know fact 1, 2, or 3?',
    '1',
    'German chocolate cake was invented in texas.',
    '2', 
    'Cleveland was onces the fifth largest city in America.', 
    '3',
    'Lemons float in water while limes sink.',
])

l_convo.train([ 
    'nothing', 
    'Ok'
])

name = input('Enter your name please: ')
bot = input('Please enter the name you would like to call the bot: ')
print("Welcome", name, 'to', bot, 'Service! I know some jokes, history facts and interesting facts.')
while True:
    request = input(name + ': ')
    if request == "Bye" or request == 'bye':
        print(bot + ': Have a good day!')
        break
    else:
        response = my_bot.get_response(request)
        print(bot + ': ', response)