#!/usr/bin/python
import traceback
import sys

commands = {'derp': 'I\'m derping!', 'fuckoff': 'I has a sad nao... :('}
try:
    with open("#fuckshit/out","r+") as f:
        f.truncate(0)
        with open("in","w", 0) as g:
            while 1:
                line = f.readline()
                if line != "":
                    message = line.split()
                    nick = message[2].strip('<>')
                    notice = message[3].strip(':')
                    if notice == 'iibot':
                        if message[4] in commands:
                            g.write("/PRIVMSG #fuckshit :" + nick + ": " + commands[message[4]] + "\n")
                        else: g.write("/PRIVMSG #fuckshit :" + nick + ": huh?\n")
                    #g.write("/PRIVMSG #fuckshit :" + nick + ": EAT A DICK\n")
except:
    print 'EXCEPTION OH FUCK\n'
    traceback.print_exc()
    f = open("#fuckshit/out","w")
    f.seek(0)
    f.truncate()
                #print line.split(" ", 3)[3][:-1]

