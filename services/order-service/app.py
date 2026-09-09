import os
from fastapi import FastAPI
import redis

app=FastAPI(title="Order Service")
r=redis.Redis(host=os.getenv("REDIS_HOST","redis"),port=6379,decode_responses=True)

def keys(): return sorted(r.scan_iter(match="order:*"))

@app.get("/health")
def health(): r.ping(); return {"service":"order-service","status":"ok"}

@app.get("/orders")
def orders():
    return [{"order_id":k.split(":",1)[1],"status":r.get(k) or "not_found"} for k in keys()]

@app.post("/orders/{order_id}", status_code=201)
def create_order(order_id:str):
    r.set(f"order:{order_id}","created")
    return {"order_id":order_id,"status":"created"}

@app.get("/orders/{order_id}")
def get_order(order_id:str):
    return {"order_id":order_id,"status":r.get(f"order:{order_id}") or "not_found"}
