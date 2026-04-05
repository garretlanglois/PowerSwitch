from datetime import datetime
from fastapi import FastAPI

from pydantic import BaseModel

import asyncio

import json

app = FastAPI()

# Credentials
BASE_URL = "http://XXXX"
AUTH = ("admin", "pwd")
HEADERS = {""}

'''
Webhook restrictions are defined on page 55
'''

# Default payload, if custom one is set change this
class PowerController(BaseModel):
    type: str
    severity: str
    message: str

@app.webhooks.post("new-subscription")
def switch_notification(body: PowerController):
    """
        Webhook is resposible for receiving notifications of different switching parameters
    """
    print("The following received:", body.type, body.severity, body.message)

@app.post("/set-webhook")
async def set_webhook(body: PowerController):
    '''Logic goes here'''