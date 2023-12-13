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
MODEL = "llama-lyric"
PROMPT = "Categorize this song based on the lyrics: happy, sad, angry, or calm"
PORT = 11434
HOST = "127.0.0.1"

def send_request(data) -> requests.Response:
    '''
    Formats the url and sends the request to ollama
    '''
    url = "http://" + HOST + ":" + str(PORT) + "/api/generate/"
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r

def format_request(song, artist, lyrics) -> dict:
    '''
    Formats the request to send to ollama
    '''
    return {"model": MODEL, "prompt": (f"{song} by {artist}:\n{lyrics}"), "stream": False}

def get_response(r) -> dict:
    '''
    Gets the response from ollama
    '''
    return r.json()

def get_output(response) -> str:
    '''
    Gets the output from the response
    '''
    return response["response"]

def main() -> None:
    '''
    Main function
    '''
    # Start the timer
    start = time.time()

    # Output string
    final_output = ""

    # Song count
    song_count = 0

    # Get the file name from the command line
    file_name = sys.argv[1]
    # Open the file
    with open(file_name, 'r') as csvfile:
        # Read the file
        reader = csv.reader(csvfile, delimiter=',')
        # Skip the header
        next(reader)
        # For each row in the file
        for row in reader:
            # Get the song name
            song = row[1]
            # Get the artist name
            artist = row[0]
            # Get the lyrics
            lyrics = row[3]
            # Format the request
            req = format_request(song, artist, lyrics)
            # Send the request to ollama
            response = send_request(req)
            # Get the response
            response = get_response(response)
            # Get the output
            output = get_output(response)
            # Append the output to the final output
            final_output += f"{song} by {artist}:\n{output}\n\n"
            # Increment the song count
            song_count += 1

        # Open the output file
        with open("output.txt", 'w') as outfile:
            # Write the output
            outfile.write(final_output)

            # Print the run time, the number of songs processed, and the average time per song
            print(f"Run time: {time.time() - start} seconds")
            print(f"Songs processed: {song_count}")
            print(f"Average time per song: {(time.time() - start) / song_count} seconds")
            exit(0)

main()
