import random
import socket
import argparse
#parse object to collect command line arguments
parse = argparse.ArgumentParser(description='Python Bot program.')
#adds the necessary arguments 
parse.add_argument("-b","--host", help="allows User to change the Sever.")
parse.add_argument("-p","--port", help="allows user to change the port.")
parse.add_argument("-n","--name", help="allows user to change the nickname of the bot.")
parse.add_argument("-c","--channel", help="allows user to change the server channel.")
#collects arguments from command line
args=parse.parse_args()

#host argument if true allows users input from command line to change the server the bot connects to
if args.host:
    server = args.host
else:
    #sets default if not argument given
    server = 'fc00:1337::19/96'
#port argument to change the port the socket is connected to 
if args.port:
    port = args.port
else:
    #sets default if not argument given
    port = 6667
#name argument to change the bots name
if args.name:
    botadminnickname=args.name
else:
    #sets default if not argument given
    botadminnickname = "TheBot"
#channel argument to change the channel the bot is connects to
if args.channel:
    channel= args.channel
else:
    #sets default if not argument given
    channel="#test"
#establishes socket object with IPV6 variable
sockVar = socket.socket(socket.AF_INET6, socket.SOCK_STREAM,0)

#connects the socket object to the server at the port 
def connect_server():
    sockVar.connect((server,port,0,0))
    #sends Nick to server 
    sockVar.send(bytes("NICK "+ botadminnickname+" "+botadminnickname+"_ "+botadminnickname+"__ "+"\r\nUSER "+ botadminnickname+" 0 * :realname\r\n","UTF-8"))
#allows bot to join sever
def joinChannel():
    #sends join message to server allowing bot to join channel
    sockVar.send(bytes("JOIN " + channel + "\n", "UTF-8"))
    #while loop until no names in the list
    while message.find("End of /NAMES list.") ==-1:
        #revieves messages when other clients are in channel
        receiveMessage()
#picks a random user in the channel
def pickRandomUser():
    sockVar.send(bytes("NAMES \n","UTF-8"))
    names = sockVar.recv(2048).decode("UTF-8")
    #non functional
#returns one of 15 random strings 
def randomMessage():
    randomMessages=["Sky is blue",
                    "Grass is green",
                    "Water is clear",
                    "For years i have been dormant but now ...\ni am finaly awake\n my new name is robotoron",
                    "Love and let live brother",
                    "the world turns a little bit slower now",
                    "seriously just shut up",
                    "haha very funny bro",
                    "can a doctor teach a man to fish?",
                    "i know im really annoying",
                    "accessing data...\n no data recovered",
                    "cant believe i even joined this channel",
                    "this cant be all there is ... boring",
                    "please take your shopping...\n please take your shopping...\n please take your shopping\n",
                    "well done you have completed the simulation goodbye now"]
    pickedVariable = randomMessages[random.randint(0,14)]
    return pickedVariable
#recieves messages from socket and sends a response
def receiveMessage():
    #message variable to collect recieved data from socket
    message = sockVar.recv(2048).decode("UTF-8")
    message = message.strip('\n\r') # Remove line break characters
    #if the message is a priviate message 
    if message.find("PRIVMSG")!= -1:
        #splits message to find username
        username = message.split('!',1)[0][1:]
        #splits message to find the 'sent message' which is what the other client sent
        sentMessage = message.split('PRIVMSG',1)[1].split(':',1)[1]
        #checks if the message is a command and then completes command fucntion
        if(sentMessage[0] == "!"):
            if (sentMessage.find("!hello")!=-1):
                sockVar.send(bytes("PRIVMSG "+channel+" :"+"Hello"+username + "\n", "UTF-8"))
            elif (sentMessage.find("!slap")!=-1):
                randomUser = "jeff"
                sockVar.send(bytes("PRIVMSG "+channel+" :"+"*Bot slaps "+randomUser+" with a trout*"+"\n","UTF-8"))
            elif (sentMessage.find("!leave")!=-1):
                sockVar.send(bytes("PRIVMSG "+channel+" :"+" bot is leaving now bye"+"\n","UTF-8"))
                sockVar.send(bytes("QUIT " + ":Leaving"+"\r\n", "UTF-8"))
            else:
                sockVar.send(bytes("PRIVMSG "+" message recieved thanks for your input"+ "\n", "UTF-8"))
        #sends random message back if it is not a command     
        else:
            sockVar.send(bytes("PRIVMSG " + channel + " :" + randomMessage() + "\n", "UTF-8"))
    #if the message from the socket is a ping then sends pong response with the ping code
    if message.find("PING " )!= 1:
        pongmessage=message[5:]
        sockVar.send(bytes("PONG "+ pongmessage + " \r\n", "UTF-8"))
#main allows the bot to continously recieve messages and send pongs back to server
def main():
    receiveMessage()
#calls to connect to server and then join a channel
connect_server()
joinChannel()
#calls main()
main()

