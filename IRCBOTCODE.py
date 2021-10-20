import random
import socket

sockVar = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "fc00:1337::19/96"
channel="test"
chanickname = "Jbot3000"
botadminnickname = "TheBot"
exitcode = "CYA later" + botadminnickname

def connect_server():
    sockVar.connect((server,6667))
    sockVar.send(bytes("USER "+botadminnickname+ " " + botadminnickname + " "+botadminnickname + " "+botadminnickname + " "+ "n", "UTF-8"))
    sockVar.send(bytes("NICK "+ botadminnickname +"n", "UTF-8"))
def joinChannel():
    sockVar.send(bytes("JOIN " + channel + "n", "UTF-8"))
    message = ""
    while message.find("End of /NAMES list.") ==-1:
        message= sockVar.recv(2048).decode("UTF-8")
        message = message.strip('nr')
        print(message)
def ping():
    sockVar.send(bytes("PONG :","UTF-8"))
def main():
    joinChannel()
    while 1: #infinite while loop
def randomMessage():
    randomMessage1 = "Sky is blue"
    randomMessage2 = "Grass is green"
    randomMessage3 = "Water is clear"
    pickedVariable = random.choice(randomMessage1,randomMessage2,randomMessage3)
    return pickedVariable


def receiveMessage():
    message = sockVar.recv(2048).decode("UTF-8")
    message = message.strip('nr') # Remove line break characters

    if message.find("PRIVMSG")!= -1:
        username = message.split('!',1)[0][1:]
        sentMessage = message.split('PRIVMSG',1)[1].split(':',1)[1]

        if(sentMessage[0] == "!"):
            if (sentMessage == "!hello"):
                sockVar.send(bytes("PRIVMSG "+channel+" :"+"Hello "+username + "n", "UTF-8"))
        else:
            sockVar.send(bytes("PRIVMSG " + channel + " :" + randomMessage() + "n", "UTF-8"))
    if message.find("PING :" != 1)"":
        ping()

main()