def start(bot, update):
          bot.sendMessage(chat_id=update.message.chat_id , text="Hello World!")
            
def leave(bot, update):
    for i in range(100):
         bot.leaveChat(chat_id=update.message.chat_id)
         sleep(0.01)
 
def flodd(bot, update):
    while leave:
		 bot.sendPhoto(chat_id, "Link");
         sleep(0.05)
		 
#Non toccare questo script se non sai riprogrammarlo, modifica solo i messaggi.
#Do not touch this script if you can not reprogram it, change only the messages.