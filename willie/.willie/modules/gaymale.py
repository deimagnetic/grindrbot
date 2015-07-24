from willie.module import commands, rate, priority
from willie import web
import re


@commands('gaymale')
def gaymale(bot, trigger):
	bot.reply("Searching for a Grindr profile as gay as you.")
	bot.reply("Sorry, none found. You are too extremely gay.")