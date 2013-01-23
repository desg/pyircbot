import socket
import requests
from weather import wUnderground
from ircparameters import ircParamaters

server, serverport = "irc.freenode.net", 6667
nick = "desgb0t"
channel = "#desgtest"
realname = nick
ident = nick

y = wUnderground('897522adf011af15')
x = ircParamaters()

s = socket.socket()
s.connect((server, serverport))
s.send("NICK %s\r\n" % nick)
s.send("USER %s %s freenode :%s\r\n" % (ident, server, realname))
s.send("JOIN :%s\r\n" % channel)

while True:
    data = s.recv(4096).lower()
    print data	
    if data.split()[0] == "ping":
        s.send("pong " + data.split()[1] + "\r\n")

    elif x.chkPrvMsg(data) == True:
        if x.ircMsg(data)[0] == "get":

            if len(x.ircMsg(data)) >= 3:

                if x.ircMsg(data)[1] == "weather":

                    weatherData = y.weather(str(x.ircMsg(data)[2]))['current_observation']
                    city = weatherData['display_location']['full']
                    cWeather = weatherData['weather']
                    temperature = weatherData['temperature_string']
                    rHumidity = weatherData['relative_humidity']
                    s.send("PRIVMSG %s :%s [weather: %s][temperature: %s][relative humidity: %s]\r\n" 
                            % (channel, city, cWeather, temperature, rHumidity))