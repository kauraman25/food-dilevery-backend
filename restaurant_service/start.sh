#!/bin/bash

# Default to port 10000 if PORT is not set
PORT=${PORT:-10000}

uvicorn main:app --host=0.0.0.0 --port=$PORT
