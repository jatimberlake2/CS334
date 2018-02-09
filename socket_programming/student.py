from socket import *
import time
from random import randint
serverName =  "10.229.71.3" #"localhost" #'10.229.121.182' #robot's IP 
serverPort = 3310
BLAZERID = "justony7"

print "START"

print "Establishing connection to robot on port 3310."
print "Creating Socket 1..."
s1 = socket(AF_INET, SOCK_STREAM)
s1.connect((serverName,serverPort))
print "Connection established"
print "Socket 1 created!"
print "Sending BlazerID to robot..."
s1.send(BLAZERID)
print "BlazerID sent"
print "Now receiving socket number for next TCP socket"
port_info = int(s1.recv(5))
s1.close()
print "Port information received, socket 1 closed"
time.sleep(1)

print "Creating Socket 2..."
s2 = socket(AF_INET, SOCK_STREAM)
print "Socket 2 established on port : <%d>" %(port_info)
print "Listening for 12 character string"
s2.bind(('0.0.0.0', port_info))
s2.listen(5)
sRobot, addr = s2.accept()
print "String accepted!"
port_info2 = sRobot.recv(12)
print "Information received!"
#sRobot is type _socketobject.
#addr is type str.
print "sRobot, addr : <%s>" %(port_info2)
pi2array = port_info2.split(",")
fffff = int(pi2array[0])
eeeee = pi2array[1]
s2.close()
print "Information parsed!"
time.sleep(1)

print "Creating Socket 3..."
s3 = socket(AF_INET, SOCK_DGRAM)
print "Socket 3 created!"
print "Generating random number between 5 and 10, noninclusive..."
rand = randint(6,9)
print "Generated integer : <%d>" %(rand)
print "Sending number to Robot..."
s3.sendto(bytes(rand), (serverName, fffff))
s3.close()
print "The number has been sent."
time.sleep(1)

print "Creating Socket 4..."
s4 = socket(AF_INET, SOCK_DGRAM)
print "Socket 4 created!"
s4.bind(('0.0.0.0', int(eeeee)))
info, addr = s4.recvfrom(10*int(rand))
print "Information received!"
xxx = bytes(info)
print "Sending long number back to Robot..."
s4.sendto(xxx, (serverName, fffff))
s4.close()
print "Information sent."
print
print "END"