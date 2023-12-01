#!/bin/bash
# Setup script for the project
# Author: Korben Tompkin
# Date: 2023-12-01

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r src/requirements.txt
