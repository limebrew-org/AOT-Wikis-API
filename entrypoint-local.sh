#!bin/bash

export PYENV=local
uvicorn server:app --host "0.0.0.0" --port 8000 --reload --workers 3