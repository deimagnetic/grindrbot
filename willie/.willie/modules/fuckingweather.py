from willie.module import commands, rate, priority, NOLIMIT
from willie import web
import re


@commands('fucking_weather', 'fw')
def fucking_weather(bot, trigger):
	text = trigger.group(2)
	if trigger.nick == "gay_kermit" or trigger.nick == "gay_kermit1":
		apple = 1+1
	else:
		if not text:
			bot.reply("INVALID FUCKING PLACE. PLEASE ENTER A FUCKING ZIP CODE, OR A FUCKING CITY-STATE PAIR.")
			return
		text = web.quote(text)
		page = web.get("http://thefuckingweather.com/?where=%s" % (text))
		temp = re.compile('<span class="temperature" tempf="(.*?)">(.*?)</span>')
		re_mark = re.compile('<p class="remark">(.*?)</p>')
		results = re_mark.findall(page)
		temper = temp.findall(page)[0]
		celsius = (round(((float(temper[0])-32)*5/9)*(0-1),1))*(0-1)
		text = text.replace("%2C",',')
		if results:
			bot.reply("IN %s IT IS %s DEGREES FARENHEIT (%s CELSIUS). %s" % (text.upper().replace("%20"," "),temper[0],celsius,results[0]))
		else:
			bot.reply("I CAN'T GET THE FUCKING WEATHER.")
 			return bot.NOLIMIT

