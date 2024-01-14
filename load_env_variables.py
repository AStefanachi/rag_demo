# from dotenv import load_dotenv

# load_dotenv("settings.env")

import os

# Get all the environmental variables
env_variables = os.environ

# Display the environmental variables
for key, value in env_variables.items():
    print(f"{key}: {value}")
