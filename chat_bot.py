#https://www.upgrad.com/blog/how-to-make-chatbot-in-python/ 
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

my_bot = ChatBot ('Kevin', storage_adapter = 'chatterbot.storage.SQLStorageAdapter', database_uri = 'sqlite:///database.sqlite3', logic_adapters = ['chatterbot.logic.BestMatch', 'chatterbot.logic.TimeLogicAdapter'],)

trainer = ListTrainer(my_bot)
#type in response for the bot below
trainer.train([])

c_trainer = ChatterBotCorpusTrainer(my_bot)
c_trainer.train('chatterbot.corpus.english')
name = input('Enter your name please: ')
print("Welcome", name, 'to Kevins Service! How can I help you today?')
while True:
    request = input(name + ': ')
    if request == "Bye" or request == 'bye':
        print('Kevin: Have a good day!')
        break
    else:
        response = my_bot.getresponse(request)
        print('Kevin: ', response)













#talk = ['Hello, how is your day?', "Hi", 'Sup', "What are you doing?", "I\ 'm good"]


#trainer = ListTrainer(bot)
#for item in (talk):
    #trainer.train(item)
#print(bot.get_response("hi"))