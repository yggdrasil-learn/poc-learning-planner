# POC Learning Planner
Initial POC chatbot application for learning planner

## Set up virtual environment

Windows:
```
pip install uv
uv venv
.venv\Scripts\activate
uv sync --dev
```

Mac/Linux:
```
pip3 install uv
uv venv
source .venv/bin/activate
uv sync --dev
```

## Start up ollama LLM

```
ollama run qwen3:0.6b
```
