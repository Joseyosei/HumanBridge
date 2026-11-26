"""Local development API; synthetic data only, no persistence or live LLM."""
from typing import Literal
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title='HumanBridge', version='0.1.0')

class PlanRequest(BaseModel):
    barrier: Literal['confidence', 'time', 'finding_people']

PLANS = {
    'confidence': 'Try greeting someone in a familiar setting.',
    'time': 'Set aside ten minutes to contact someone you trust.',
    'finding_people': 'Explore a group centred on a hobby you enjoy.',
}

@app.get('/health')
def health():
    return {'status': 'ok', 'mode': 'prototype'}

@app.post('/v1/plan')
def plan(request: PlanRequest):
    return {'action': PLANS[request.barrier], 'mode': 'rule_based_demo'}
