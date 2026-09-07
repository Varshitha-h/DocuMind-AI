#!/bin/bash

ollama serve &
sleep 5

ollama pull llama3.2

uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}