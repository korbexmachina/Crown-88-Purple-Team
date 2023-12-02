# Interpreter for the project
# Author: Korben Tompkin
# Date: 2023-12-01

# Uses ollama to interpret the data from csv files
# Communicates with ollama via http requests

import requests
import json
import time
import os
import sys
import csv

# Global variables
MODEL = "llama2"
PROMPT = "Catagorize this song based on the lyrics: happy, sad, angry, or calm"
PORT = 11434
HOST = "127.0.0.1"

def send_request(data) -> requests.Response:
    '''
    Formats the url and sends the request to ollama
    '''
    url = "http://" + HOST + ":" + str(PORT) + "/api/generate/"
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, data=json.dumps(format_request(data)), headers=headers)
    return r

def format_request(data) -> dict:
    '''
    Formats the request to send to ollama
    '''
    return {"model": MODEL, "prompt": data, "stream": False}

def get_response(r) -> dict:
    '''
    Gets the response from ollama
    '''
    return r.json()

def get_prediction(response) -> str:
    '''
    Gets the prediction from the response
    '''
    return response["response"]

def main():
    '''
    Main function
    '''
    # Get the file name from the command line
    file_name = sys.argv[1]
    # Open the file
    with open(file_name, newline='') as csvfile:
        # Read the file
        reader = csv.reader(csvfile, delimiter=',')
        # Skip the header
        next(reader)
        # For each row in the file
        for row in reader:
            # Get the lyrics
            lyrics = row[5]
            # Send the request to ollama
            response = send_request(lyrics)
            # Get the response
            response = get_response(response)
            # Get the prediction
            prediction = get_prediction(response)
            # Print the prediction
            print(prediction)

if __name__ == "__interpreter__":
    main()
