import os
from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector

app = FastAPI(title="User Service")

class User(BaseModel):
    name: str
    email: str

def db(): return mysql.connector.connect(host=os.getenv("MYSQL_HOST","mysql"),database=os.getenv("MYSQL_DATABASE","ecommerce"),user=os.getenv("MYSQL_USER","app"),password=os.getenv("MYSQL_PASSWORD","app_password"))

@app.get("/health")
def health(): return {"service":"user-service","status":"ok"}

@app.get("/users")
def users():
    conn=db(); cur=conn.cursor(dictionary=True); cur.execute("SELECT id,name,email FROM users ORDER BY id"); rows=cur.fetchall(); cur.close(); conn.close(); return rows

@app.post("/users", status_code=201)
def create_user(user: User):
    conn=db(); cur=conn.cursor(); cur.execute("INSERT INTO users (name,email) VALUES (%s,%s)",(user.name,user.email)); conn.commit(); user_id=cur.lastrowid; cur.close(); conn.close(); return {"id":user_id,"name":user.name,"email":user.email}
