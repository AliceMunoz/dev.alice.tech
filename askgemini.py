!/bin/bash

API_KEY="tu_api_key_de_gemini"
API_URL="https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=${API_KEY>

if [ -z "$1" ]; then
  echo "Usage: askgemini \"Your question here\""
  exit 1
fi

QUERY="$1"

RESPONSE=$(curl -s -H 'Content-Type: application/json' -d "{\"contents\":[{\"parts\":[{\"text\":\"$QUERY\"}]}]}" -X PO>

# Parsea la respuesta para obtener solo el texto
echo "$RESPONSE" | grep -o '"text": ".*"' | cut -d '"' -f 4
