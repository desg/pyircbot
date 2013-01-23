#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
#  
#  Copyright 2013 Demetrius Mahone <desg@ubuntu>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import requests

class ElophantLibrary():
	
	def __init__(self, key):
		self.Elophant = "http://api.elophant.com/v2/"
		self.key = key
		
	def get_summoner(self, Reigon, SummonerName):
		return requests.get(self.Elophant + Reigon + "/summoner/" 
			+ SummonerName, params = {'key': self.key}).json()
		
	def get_master_pages(self, Reigon, SummonerId):
		return requests.get(self.Elophant + Reigon + "/mastery_pages/" 
			+ str(SummonerId), params = {'key': self.key}).json()
			
	def get_rune_pages(self, Reigon, SummonerId):
		return requests.get(self.Elophant + Reigon + "/rune_pages" 
			+ str(SummonerId), params = {'key': self.key}).json()
			
	def get_recent_games(self, Reigon, AccountId):
		return requests.get(self.Elophant + Reigon + "/recent_games/"
			+ str(AccountId), params = {'key': self.key}).json()
			
	def get_summoner_names(self, Reigon, SummonerIds):
		#Use a comma to seperate SummonerIds
		#Example 71500,19307647,125586,19135198
		return requests.get(self.Elophant + Reigon + "/summoner_names/"
			+ SummonerIds, params = {'key': self.key}).json()
	
	def get_player_stats(self, Reigon, AccountId, Season):
		#The attributes for season are current , two, and one
		return requests.get(self.Elophant + Reigon + "/player_stats/"
			+ AccountId + "/" + Season, 
				params = {'key' : self.key}).json()
				
	def get_ranked_stats(self, Reigon, AccountId, Season):
		return requests.get(self.Elophant + Reigon + "/ranked_stats/"
			+ AccountId + "/" + Season,
				params = {'key' : self.key}).json()

	def get_summoner_team_info(self, Reigon, SummonerId):
		return requests.get(self.Elophant + Reigon 
			+ "/summoner_team_info/" + SummonerId,
				params = {'key' : self.key}).json()
				
	def get_in_progress_game_info(self, Reigon, SummonerName):
		return requests.get(self.Elophant + Reigon 
			+ "/in_progress_game_info/" + SummonerName,
				params = {'key' : self.key}).json()

	def get_team(self, Reigon, TeamId):
		return requests.get(self.Elophant + Reigon + "/team/" + TeamId,
			params = {'key' : self.key}).json()
			
	def get_find_team(self, Reigon, TeamTag):
		#Will add Url encoding for Team names later
		#Use initials for now
		return requests.get(self.Elophant + Reigon + "/find_team/" 
			+ TeamTag, params = {'key' : self.key}).json()
			
	def get_team_end_of_game_stats(self, Reigon, TeamId, GameId):
		return requests.get(self.Elophant + Reigon + "/team/"
			+ TeamId + "/end_of_game_stats/" + GameId,
				params = {'key' : self.key}).json()
				
	def get_team_ranked_stats(self, Reigon, TeamId):
		return requests.get(self.elophant + Reigon + "/team/" + TeamId
			+ "/ranked_stats", params = {'key': self.key}).json()
