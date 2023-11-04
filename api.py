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

from typing import Annotated
from fastapi import Body,FastAPI
from fastapi.middleware.cors import CORSMiddleware

#------------------------#
#   INITIALIZE FastAPI   #
#------------------------#

app = FastAPI()                                     # Creates FastAPI App
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#---------------------------#
#   SANITY CHECK ENDPOINT   #
#---------------------------#

@app.get("/sanitycheck")                            # Sanity check endpoint to ensure server is accessible
async def sanity_check():
    return {"message": "Get request successful"}



