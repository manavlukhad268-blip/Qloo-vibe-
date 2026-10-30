```python
import os
import random
import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Qloo-vibe API Engine")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

QLOO_API_KEY = os.getenv("QLOO_API_KEY", "")
QLOO_BASE_URL = "https://hackathon.api.qloo.com"

class QueryRequest(BaseModel):
    seed_entity: str
    category: str = "Music"
    audience: str = "Gen-Z"

def get_mock_data(seed: str):
    return {
        "status": "success",
        "source": "Simulated Live Engine",
        "seed": seed,
        "persona": "Cyber-Minimalist Creator",
        "scores": {"Music": 94, "Movies": 91, "Fashion": 88, "Dining": 82, "Travel": 89},
        "dna": {
            "music": ["Hans Zimmer", "M83"],
            "movies": ["Blade Runner 2049", "Ex Machina"],
            "fashion": ["Techwear Minimal"],
            "dining": ["Artisanal Espresso Labs"],
            "travel": ["Tokyo (Shibuya)", "Berlin"]
        }
    }

@app.post("/api/analyze")
def analyze(req: QueryRequest):
    if not QLOO_API_KEY:
        return get_mock_data(req.seed_entity)
    
    try:
        res = requests.get(
            f"{QLOO_BASE_URL}/search",
            headers={"X-Api-Key": QLOO_API_KEY},
            params={"query": req.seed_entity, "type": req.category.lower()},
            timeout=4
        )
        return res.json() if res.status_code == 200 else get_mock_data(req.seed_entity)
    except Exception:
        return get_mock_data(req.seed_entity)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
