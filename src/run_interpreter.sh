# Script to automate running the interpreter program
# Author: Korben Tompkin
# Date: 2023-12-13

# Accept an arbitrary number of arguments that are all input files

echo "Running interpreter on $@"

# Check if the virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment"
    python3 -m venv venv
fi

# Start the virtual environment
source venv/bin/activate

# Install the requirements
pip install -r requirements.txt

for file in "$@"
do
    echo "Running $file"
    python3 interpreter.py data/$file
done
