#    ___              __         ____    __      __  ___         __                     __
#   / _ \___ ___ ____/ /_ __    / __/__ / /_    /  |/  /__  ____/ /____ ____ ____ ____ / /
#  / , _/ -_) _ `/ _  / // /   _\ \/ -_) __/   / /|_/ / _ \/ __/ __/ _ `/ _ `/ _ `/ -_)_/ 
# /_/|_|\__/\_,_/\_,_/\_, ( ) /___/\__/\__( ) /_/  /_/\___/_/  \__/\_, /\_,_/\_, /\__(_)  
#                    /___/|/              |/                      /___/     /___/ 
#
# Ready, Set, Mortgage! API
# Authors: 

#-------------#
#   IMPORTS   #
#-------------#

import os
from dotenv import load_dotenv
from typing import Annotated
from fastapi import Body,FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai


#------------------------#
#   INITIALIZE FASTAPI   #
#------------------------#

app = FastAPI()                                     # Creates FastAPI App
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)                                                   # Allows cross-origin requests


#-----------------------#
#   INITIALIZE OPENAI   #
#-----------------------#

load_dotenv()                                       # Loads environment variables from a .env file if present for local development
OPENAI_KEY = os.getenv('OPENAI_KEY')                # Imports OpenAI key from environment variable


#-----------------------#
#   DEFINE DATA MODEL   #
#-----------------------#

class UserStats(BaseModel):
    gross_monthly_income: float
    monthly_car_payment: float
    monthly_credit_card_payment: float
    student_loan_payment: float
    home_appraised_value: float
    est_monthly_mortgage_payment: float
    down_payment_amount: float
    credit_score: int


#---------------------------#
#   SANITY CHECK ENDPOINT   #
#---------------------------#

@app.get("/sanity_check")                            # Sanity check endpoint to ensure server is accessible
async def sanity_check():
    return {
        "message": "Get request successful"
    }


#---------------------------------#
#   MORTGAGE READINESS ENDPOINT   #
#---------------------------------#

@app.post("/readiness")
async def readiness():
    return {
        'readiness': 'Placeholder',
        'breakdown': {
            'credit': {
                'individual_readiness': 'Placeholder',
                'score': -1.0
            },
            'ltv': {
                'individual_readiness': 'Placeholder',
                'score': -1.0
            },
            'dti': {
                'individual_readiness': 'Placeholder',
                'score': -1.0
            },
            'fedti': {
                'individual_readiness': 'Placeholder',
                'score': -1.0
            }
        },
        'notices': ['Placeholder']
    }
