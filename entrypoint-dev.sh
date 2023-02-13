#!bin/bash

export PYENV=dev
uvicorn server:app --host "0.0.0.0" --port 8000 --reload 