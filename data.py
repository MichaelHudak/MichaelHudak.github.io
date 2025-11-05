"""
Access the Open Trivia DB API for 10 random trivia questions.
Read the API documentation: https://opentdb.com/api_config.php

 - The type should remain as 'boolean' for the true/false format of the quiz game
 - Feel free to add 'category' and 'difficulty' parameters
"""
import requests

parameters = {
    "amount" : 10,
    "type" : "boolean"
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()["results"]
