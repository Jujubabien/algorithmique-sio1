import socket, sys, math, time

def calcul(nb1,nb2):
    resultat=nb1**0.5
    resultat=resultat*nb2
    resultat=round(resultat,2)
    return resultat


server = "irc.root-me.org"       #settings
channel = "#root-me_challenge"
botnick = "jujubabien"
input('wait1')
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#defines the socket    
input('wait2')
print("connecting to:"+server)
input('wait3')
irc.connect((server, 6667))  
input('wait4')                                                       
#connects to the server
irc.send(bytes("USER "+ botnick +" "+ botnick +" "+ botnick +" :This is a fun bot!\n","UTF-8"))
#user authentication
input('wait5')
irc.send(bytes("NICK "+ botnick +"\n","UTF-8")) 
#sets nick
input('wait6')
irc.send(bytes("JOIN "+ channel +"\n","UTF-8"))   
#join the chan
input('wait7')
irc.send(bytes("MSG NickServ IDENTIFY 'foutriquet'","UTF-8"))                           
irc.send(bytes("PRIVMSG candy !ep1\r\n","UTF-8"))
text=irc.recv(2040)
print(text) 
text=irc.recv(2040)
print(text) 
text=irc.recv(2040)
print(text) 
text=irc.recv(2040)
print(text) 
text=irc.recv(2040)
print(text) 
text=irc.recv(2040)
irc.send(bytes("PRIVMSG candy !ep1\r\n","UTF-8"))


   
  
  
#auth        

while 1:
    #puts it in a loop
    text=irc.recv(2040)
    print(text) 
 
    #receive the text
    if (text.find(b'PING') != -1):
        #check if 'PING' is found
        irc.send(b'PONG ' + text.split()[1] + b'\r\n') 
        #returns 'PONG' back to the server (prevents pinging out!)
    if (text.find(b'Candy') != -1 and text.find(b'/') != -1):
        extract=text.split(b'jujubabien :')
        print(extract)
        nb1,nb2=extract[1].split(b'/')
        nb1=nb1.decode().strip()
        nb2=nb2.decode().strip().replace("\r\n","")
        print(nb1,nb2)
        retour =str(calcul(float(nb1),float(nb2)))
        irc.send(bytes("PRIVMSG candy !ep1 -rep "+retour+"\r\n","UTF-8"))
        time.sleep(2)
   