import socket
def connect_server():
    sockVar = socket.socket(socket.AF_INET, socket.SOCK_STREAM)server = "fc00:1337;;19/96"
    Channel="test"
    chanickel = "Jbot3000"
    nick = "TheBot"
    exitcode= "CYA later" + chanickel
    sockVar.connect((server,6667))
    sockVar.send(bytes("USER "+adminNick+ " " + adminNick + " "+adminNick + " "+adminNick + " "+ "n", "UTF-8"))
    sockVar.send(bytes("NICK "+ chanickel +"n", "UTF-8"))
def joinChannel(channel):
    sockVar.send(bytes("JOIN " + channel + "n", "UTF-8"))
    message = ""
    while message.find("End of /NAMES list.") ==-1:
        message= sockVar.recv(2048).decode("UTF-8")
        message = message.strip('nr')
        print(message)
        
                                
