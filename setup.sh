#!/bin/bash
# Setup script for the project
# Author: Korben Tompkin
# Date: 2023-12-01

# Check if python3 is installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 could not be found"
    exit
fi

# Check if pip is installed
if ! command -v pip &> /dev/null
then
    echo "Pip could not be found"
    exit
fi

# Check if there is an existing virtual environment
# If there is, ask if the user wants to delete it
if [ -d "venv" ]
then
    echo "A virtual environment already exists"
    read -p "Do you want to delete it? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]
    then
        rm -rf venv
    else
        exit
    fi
fi

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r src/requirements.txt
