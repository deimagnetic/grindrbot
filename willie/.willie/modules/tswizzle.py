import willie
import json
import re
import sys
import random

@willie.module.commands("tswizzle")
def tswizzle(bot, trigger):
	numb = int(round(random.randrange(0,30),0))
	songlist = ['Shake It Off','Blank Space','You Belong With Me','We Are Never Ever Getting Back Together','22','I Knew You Were Trouble','Love Story','Mine','Everything Has Changed ft. Ed Sheeran','Mean','Our Song','Back To December','White Horse','Fifteen','Teardrops On My Guitar','Begin Again','Safe & Sound feat. The Civil Wars (The Hunger Games: Songs from District 12 and Beyond)','The Story of Us','Picture to Burn','Red','Style','Change','Riptide Cover','Fearless','Sparks Fly',"I'm Only Me When I'm With You",'Ours','The Last Time ft. Gary Lightbody','Both of Us ft. BoB','Tim McGraw']
	linklist = ['https://www.youtube.com/watch?v=nfWlot6h_JM','https://www.youtube.com/watch?v=e-ORhEE9VVg','https://www.youtube.com/watch?v=VuNIsY6JdUw','https://www.youtube.com/watch?v=WA4iX5D9Z64','https://www.youtube.com/watch?v=AgFeZr5ptV8','https://www.youtube.com/watch?v=vNoKguSdy4Y','https://www.youtube.com/watch?v=8xg3vE8Ie_E','https://www.youtube.com/watch?v=XPBwXKgDTdE','https://www.youtube.com/watch?v=w1oM3kQpXRo','https://www.youtube.com/watch?v=jYa1eI1hpDE','https://www.youtube.com/watch?v=Jb2stN7kH28','https://www.youtube.com/watch?v=QUwxKWT6m7U','https://www.youtube.com/watch?v=D1Xr-JFLxik','https://www.youtube.com/watch?v=Pb-K2tXWK4w','https://www.youtube.com/watch?v=xKCek6_dB0M','https://www.youtube.com/watch?v=cMPEd8m79Hw','https://www.youtube.com/watch?v=RzhAS_GnJIc','https://www.youtube.com/watch?v=nN6VR92V70M','https://www.youtube.com/watch?v=yCMqcFAigRg','https://www.youtube.com/watch?v=Zlot0i3Zykw','https://www.youtube.com/watch?v=-CmadmM5cOk','https://www.youtube.com/watch?v=B1jYllE0T-k','https://www.youtube.com/watch?v=2GGRdwfhl-U','https://www.youtube.com/watch?v=ptSjNWnzpjg','https://www.youtube.com/watch?v=oKar-tF__ac','https://www.youtube.com/watch?v=AlTfYj7q5gQ','https://www.youtube.com/watch?v=LZ34LlaIk88','https://www.youtube.com/watch?v=QuijXg8wm28','https://www.youtube.com/watch?v=1sa9qeV6T0o','https://www.youtube.com/watch?v=GkD20ajVxnY']
	if trigger.nick == "gay_kermit" or trigger.nick =="gay_kermit1":
		apple = 1+1
	else:
    		bot.reply("You randomed the song Taylor Swift - " + songlist[numb])
    		bot.say(linklist[numb])

