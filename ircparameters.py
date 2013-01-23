class ircParamaters():

	def ircMsg(self, data):# gets the irc message and splits it into a list 
		return data.split(":")[2].split()

	def ircChn(self, data):# gets the name of the irc channel
		return data.split(":")[1].split()

	def ircNck(self, data):# gets the nick of a user who talks 
		return data.split(":")[1].split("!")

	def chkPrvMsg(self, data):# checks if it's a private message

		if data.split(":")[0] == "":
			if data.split(":")[1].split()[1].lower() == "privmsg":
				return True
			else:
				return False