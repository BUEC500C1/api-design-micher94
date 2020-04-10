# Michaela Reardon
# EC500: Homework 2

import json
import requests
import csv
import time


class Airport:
	def __init__(self,ident,iata,coord):
		self.ident = ident
		self.__dict__[iata] = coord
		return



# Levereged information from this youtube video on how to use the Open weather API: https://www.youtube.com/watch?v=lcWfSn6-m_8

def weatherdata(iata):
# def main():

	filename = "airport-codes.csv"
	Airports=dict()
	# read the csv file
	with open(filename,encoding='utf-8') as csvDataFile:
		csvReader=csv.reader(csvDataFile)
		for row in csvReader:
			coord=row[11].split()
			# print(coord)
			if len(coord)>1:
				# print(len(coord))
				# time.sleep(2)
				# print(coord[0][:-1])
				# print(coord[1])
				entry=coord[0][:-1]+','+coord[1]
				# print(entry)
				Airports[row[9]]=entry

	# print(Airports[iata])



	try:
		Coord = Airports[iata]
		Timeframe = 'now'

		# print(Coord)

		# This commented line is how to do it using the Open Weather API. The Key is not included
		# api_access = 'http://api.openweathermap.org/data/2.5/weather?appid=&q=Boston'

		# This next line is how to access with the Weather API
		api_access_bare = 'https://api.weather.gov/points/'
		# Combine the bare api link with the coordinates input by the user
		api_access = api_access_bare + Coord
		# print(api_access)
		
		
		json_data = requests.get(api_access).json()
		# print(json_data)

		# from the initial json data, find the link to the forecast data
		forecast_access = json_data['properties']['forecast']
		# print(forecast_access)

		# request the forecast data
		new_json_data = requests.get(forecast_access).json()
		# print(new_json_data)

		# go through the available forcast data based on the timeframe name and pull the one most similar to the user.
		if Timeframe=='now':
			for periods in new_json_data['properties']['periods']:
			# print(periods['name'])
				if periods['number']==1:
					temp = periods['temperature']
					units = periods['temperatureUnit']
					# print(periods['temperature'], periods['temperatureUnit'])
		else:
			for periods in new_json_data['properties']['periods']:
				# print(periods['name'])
				if periods['name']==Timeframe:
					temp = periods['temperature']
					units = periods['temperatureUnit']
					print(periods['temperature'], periods['temperatureUnit'])
		print(temp,units)
		return True
	except KeyError as error:
		print('I am an exception')
		return False
	else:
		return False


if __name__ == '__main__':
	main()

