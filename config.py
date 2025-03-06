import os
from dotenv import load_dotenv

# Get your local configurations like PWs and User Names from "localconfig.env"
load_dotenv('localconfig.env')

# get the environment variables
DATABASE_URL = os.getenv("DATABASE_URL")
