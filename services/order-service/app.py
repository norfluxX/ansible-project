import os
from fastapi import FastAPI
import redis

app = FastAPI(title="Order Service")
r = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379, decode_responses=True)

@app.get("/health")
def health():
    r.ping()
    return {"service": "order-service", "status": "ok"}

@app.post("/orders/{order_id}")
def create_order(order_id: str):
    r.set(f"order:{order_id}", "created")
    return {"order_id": order_id, "status": "created"}

@app.get("/orders/{order_id}")
def get_order(order_id: str):
    return {"order_id": order_id, "status": r.get(f"order:{order_id}") or "not_found"}
