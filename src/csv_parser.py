# Purple Team CSV Parser
# Reads in the Billboard Hot 100 Dataset and the Spotify Dataset
# Creates a CSV file for each year with the following columns:
#   - Song Name
#   - Artist
#   - Date (From charts.csv)
#   - Lyrics
# Only using Data from 2011-2021

import csv
import os
import sys
import pandas as pd

