import willie
import time

@willie.module.commands("timer")
def timer(bot, trigger):
	if trigger.nick == "gay_kermit" or trigger.nick =="gay_kermit1":
		apple = 1+1
	else:
		timed = trigger.split(" ")
		if len(timed)==3:
			if timed[2]=="s" or "sec" or "secs":
				time.sleep(float(timed[1]))
			elif timed[2]=="min" or "m" or "mins":
				time.sleep(float(int(timed[1])*60))
			elif timed[2]=="hours" or "hr" or "hour":
				time.sleep(float(int(timed[1])*3600))
			else:
				bot.reply("Please enter a valid time format")
			bot.reply("Timer is up!")
    		else:
			bot.reply("Please reenter with seconds, minutes, or hours. For example: .timer 1 m")
