from telegram.ext import Updater, CommandHandler
import logging
from time import sleep
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

from past.builtins import execfile

execfile('script.py')
        
def main():
    updater = Updater('Your Token') #Inserisci il tuo token al posto di: Your Token.
 
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('flodd', flodd))
    updater.dispatcher.add_handler(CommandHandler('leave', leave))
 
    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main()
	
#Non toccare questo script se non sai riprogrammarlo, inserisci solo il token del bot.
#Do not touch this script if you can not reprogram it, just insert the token bot.