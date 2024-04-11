# Ollama Demo

1. Create and activate virtual environment:

`pyenv virtualenv 3.11 ollama-demo-py311`

`pyenv local ollama-demo-py311`

`pyenv activate ollama-demo-py311.`

2. Install some libraries:

`pip install ollama langchain chromadb`

3. Run ollama and pull the models used:

`ollama pull codellama:7b-code`

`ollama pull gemma:7b`

`ollama pull nomic-embed-text`

`ollama pull llava`

4. Run the demo scripts:

`python ./gemma-2.py`

# License

Distributed under the MIT License. See `LICENSE.txt` for more information.
