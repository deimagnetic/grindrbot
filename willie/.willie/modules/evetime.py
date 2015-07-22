from datetime import datetime
import willie.module
from time import gmtime, strftime
@willie.module.commands('et')
def currentevetime(bot, trigger):
        et = strftime("Current Eve Time: %m/%d/%Y - %H:%M:%S", gmtime())#str(datetime.utcnow())#strftime("%Y-%m-%d %H:%M:%S", datetime.utcnow())
	bot.say(et)


