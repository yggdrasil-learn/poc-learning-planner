 :deciduous_tree: POC Learning Planner
Initial POC chatbot application for learning planner

## :package: Set up virtual environment

Windows:
```
pip install uv
uv venv
.venv\Scripts\activate
uv python install 3.12.10
uv sync --dev
```

Mac/Linux:
```
pip3 install uv
uv venv
source .venv/bin/activate
uv python install 3.12.10
uv sync --dev
```

## :brain: Start up ollama LLM

```
ollama run qwen3:0.6b
```

## :rocket: Launch streamlit application

```
streamlit run src/Home.py
```

## :test_tube: Code Analysis

### Code complexity

```
complexipy .
```

### Unit tests

```
pytest --log-file=pytest.log tests/
```

### Linting

```
ruff check --output-format concise -o ruff.log
```

### Type Checking

```
ty check --output-format concise . > ty.log
```

