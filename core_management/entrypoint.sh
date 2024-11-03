#!/bin/sh
echo "Running tests..."
pytest core_management/tests

if [ $? -ne 0 ]; then
    echo "Tests failed. Exiting."
    exit 1
fi

echo "Tests passed. Starting server..."
python main.py
