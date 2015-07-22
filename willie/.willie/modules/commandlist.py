import willie

@willie.module.commands("working")
def workingcommands(bot, trigger):
	if trigger.nick == "gay_kermit" or trigger.nick == "gay_kermit1":
		apple = 1+1
	else:	
		bot.say("My working list of commands can be found at: http://goo.gl/wJpfsz")

@willie.module.commands("commands")
def commands(bot, trigger):
    	if trigger.nick == "gay_kermit" or trigger.nick == "gay_kermit1":
		apple = 1+1
	else:
		bot.say("My working list of commands can be found at: http://goo.gl/wJpfsz")
