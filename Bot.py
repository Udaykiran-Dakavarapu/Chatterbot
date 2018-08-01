from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

bot=ChatBot("Uday",
    read_only=False
)
bot.set_trainer(ChatterBotCorpusTrainer)

bot.train(
    "chatterbot.corpus.english"
)

#for files in os.listdir('C:/Users/Kiran/Desktop\chatterbot-corpus-master\chatterbot-corpus-master\chatterbot_corpus\data\english/'):
#    data=open('C:/Users/Kiran/Desktop\chatterbot-corpus-master\chatterbot-corpus-master\chatterbot_corpus\data\english/' + files , 'r').readlines()
#    bot.train(data)
while True:
    message = input("Me:")
    if(message.strip()=='Bye' or message.strip()=='bye'):
        print("Bot replied: Bye")
        break
    if(message.strip()!='Bye' or message.strip()!='bye'): 
        reply=bot.get_response(message)
        print("Bot replied:",reply)
        
    
    
