from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer 

app = Flask(__name__)

my_bot = ChatBot('Kevin', read_only = True, storage_adapter = 'chatterbot.storage.SQLStorageAdapter',  logic_adapters = ['chatterbot.logic.BestMatch', 'chatterbot.logic.TimeLogicAdapter'], database_uri = 'sqlite:///database.sqlite3',)
trainer = ChatterBotCorpusTrainer(my_bot)
trainer.train('chatterbot.corpus.english.greetings', 'chatterbot.corpus.english.converstaions')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get')
def get_bot_response():
    userText = request.args.get('msg')
    return str(my_bot.get_response(userText))

if __name__ == "__main__":
    app.run()