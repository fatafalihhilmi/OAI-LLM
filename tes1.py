from dotenv import load_dotenv, find_dotenv
import os

# Find and load the .env file
dotenv_path = find_dotenv('api.env')
load_dotenv(dotenv_path)

# Get the API key
api_key = os.getenv('API_KEY')

print(f'API Key: {api_key}')