#!/bin/bash
echo "{ \"event\": \"install-start\" }"
if [ ! -d "venv" ]; then
    echo "{ \"event\": \"create-venv\" }"
    python -m venv venv
else
    echo "venv folder already exists, skipping creation..."
fi
echo "{ \"event\": \"activate-venv\" }"
source venv/bin/activate

#pip install --use-pep517 --upgrade -r requirements.txt
echo "{ \"event\": \"install-requirements\" }"
if pip install --use-pep517 --upgrade -r requirements.txt; then
    echo "Successfully installed requirements"
    echo "{ \"event\": \"install-success\" }"
    exit 0
else
    echo "Failed to install requirements"
    echo "{ \"event\": \"install-failure\" }"
    exit 1
fi

