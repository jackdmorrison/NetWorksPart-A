import random
import socket
import argparse

parse = argparse.ArgumentParser(description='Python Bot program.')

parse.add_argument("-b","--host", help="allows User to change the Sever.")
parse.add_argument("-p","--port", help="allows user to change the port.")
parse.add_argument("-n","--name", help="allows user to change the nickname of the bot.")
parse.add_argument("-c","--channel", help="allows user to change the server channel.")
args=parse.parse_args()

if args.host:
    server = args.host
else:
    server = 'fc00:1337::19/96'
if args.port:
    port = args.port
else:
    port = 6667
if args.name:
    botadminnickname=args.name
else:
    botadminnickname = "TheBot"
if args.channel:
    channel= args.channel
else:
    channel="#test"
sockVar = socket.socket(socket.AF_INET6, socket.SOCK_STREAM,0)



exitcode = "CYA later" + botadminnickname

def connect_server():
    sockVar.connect((server,port,0,0))
    
    sockVar.send(bytes("NICK "+ botadminnickname+"\r\nUSER "+ botadminnickname+"0 * :realname\r\n","UTF-8"))
    #sockVar.send(bytes("NICK "+ botadminnickname +"/n", "UTF-8"))
def joinChannel():
    sockVar.send(bytes("JOIN " + channel + "\n", "UTF-8"))
    message = ""
    while message.find("End of /NAMES list.") ==-1:
        message= sockVar.recv(2048).decode("UTF-8")
        message = message.strip('nr')
        print(message)
def main():
    joinChannel()
    #while 1:
        #infinite while loop


def randomMessage():
    
    randomMessage1 = "Sky is blue"
    randomMessage2 = "Grass is green"
    randomMessage3 = "Water is clear"
    randomMessage4 = "For years i have been dormant but now i am finaly awake my new name is robotoron"
    randomMessage5 = "Love and let live brother"
    randomMessage6 = "the world turns a little bit slower now"
    randomMessage7 = "seriously just shut up"
    randomMessage8 = "haha very funny bro"
    randomMessage9 = "can a doctor teach a man to fish?"
    randomMessage10 = "sorry for your loss"
    randomMessage11 = "accessing data.../n no data recovered"
    randomMessage12 = "cant believe i even joined this channel"
    randomMessage13 = "this cant be all there is ... boring"
    randomMessage14 = "please take your shopping.../n please take your shopping.../n please take your shopping/n"
    randomMessage15 = "well done you have completed the simulation goodbye now"
    pickedVariable = random.choice(randomMessage1,randomMessage2,randomMessage3,randomMessage4,randomMessage5,randomMessage6,randomMessage7,randomMessage8,randomMessage9,randomMessage10,randomMessage11,randomMessage12,randomMessage13,randomMessage14,randomMessage15)
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
            elif (sentMessage == "!slap"):
                randomUser = pickRandomUser()
                sockVar.send(bytes("PRIVMSG "+channel+" :"+"*Bot slaps "+randomUser+" with a trout*"+"n","UTF-8"))
            else:
                sockVar.send(bytes("PRIVMSG "+" message recieved thanks for your input"+ "n", "UTF-8"))
                
        else:
            sockVar.send(bytes("PRIVMSG " + channel + " :" + randomMessage() + "n", "UTF-8"))
    if message.find("PING :" != 1):
        sockVar.send(bytes("PONG :", "UTF-8"))
connect_server()
main()

