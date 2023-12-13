# Crown-88-Purple-Team

## Usage

1. Clone the repository and cd into it

2. Build the model from the Modelfile
    - `ollama create lyric-llama -f ./Modelfile`

3. cd into the src directory

4. Add your csv files to the `data` directory

5. Run the following command, providing the files you want to use as arguments
    - `./run_interpreter.sh <File1> <File2> ... <FileN>`
    - __Note:__ The file paths will be interpreted relative to the data directory.

## System Dependencies

- [Ollama](https://ollama.ai/)
- [Python3](https://www.python.org/)
