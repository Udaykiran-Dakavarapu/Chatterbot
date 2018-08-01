from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

bot=ChatBot("Uday")
bot.set_trainer(ListTrainer)


for files in os.listdir('C:/Users/Kiran/Desktop\chatterbot-conversations/'):
    data=open('C:/Users/Kiran/Desktop\chatterbot-conversations/'+ files , 'r').readlines()
    bot.train(data)
while True:
    message = input("Me:")
    if(message.strip()!='Bye' or message.strip()!='bye'): 
        reply=bot.get_response(message)
        print("Bot replied:",reply)
    if(message.strip()=='Bye' or message.strip()=='bye'):
        print("Bot replied: Bye")
        break
        
    
    
