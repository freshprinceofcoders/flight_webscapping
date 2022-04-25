from urllib import response
import requests
import json
import smtplib
import ssl

from flight_fare import FlightFare


def getFlightData(inputData):

    print(inputData)#this gets all the data from the html to parse to the API
    source = inputData['origin']
    destination = inputData['destination']
    departureDate = inputData['departureDate']
    returnDate = inputData['returnDate']
    seatType = inputData['class']
    budget = inputData['budget']



    url = f"https://api.flightapi.io/roundtrip/620fd0a4853d6d634dae50e2/{source}/{destination}/{departureDate}/{returnDate}/1/0/0/{seatType}/GBP" #This sends the information to the API so that it can get the flight data from it and return it to the user 

    response = requests.get(url)#returns the result of the API 

    print("Flight api response: 1 ")
    print(response)#gets a response of 200
    the_info = response.json()
    #print (the_info)
    if response.status_code == 200:#this will return the flight details if the route is available 
        options = the_info['fares']
    else:
        options = []#will return nothing 

    results = ""
    for option in options:

        if int(budget) >= option['price']['amount']:#This just checks if the amount returned is less than teh budget
            flight_fare = FlightFare(
                option['price']['amount'], option['handoffUrl'])
            results += flight_fare.get_flight_price()
            return flight_fare

    return "Prices not found"

    '''
    
    
    
    
    
    i=0
    #print(int(user_input[8]))
    for i in range(len(the_info['Quotes'])):
        if int(user_input[8]) >= int(the_info['Quotes'][i]["MinPrice"]):
            print(int(the_info['Quotes'][i]['MinPrice']))            
        i+=1
    '''
# readFile('flightData.json')