import os
from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector

app = FastAPI(title="Product Service")

class Product(BaseModel):
    name: str
    price: float

def db():
    return mysql.connector.connect(host=os.getenv("MYSQL_HOST", "mysql"), database=os.getenv("MYSQL_DATABASE", "ecommerce"), user=os.getenv("MYSQL_USER", "app"), password=os.getenv("MYSQL_PASSWORD", "app_password"))

@app.get("/health")
def health(): return {"service":"product-service","status":"ok"}

@app.get("/products")
def products():
    conn=db(); cur=conn.cursor(dictionary=True); cur.execute("SELECT id,name,price FROM products ORDER BY id"); rows=cur.fetchall(); cur.close(); conn.close(); return rows

@app.post("/products", status_code=201)
def create_product(product: Product):
    conn=db(); cur=conn.cursor(); cur.execute("INSERT INTO products (name,price) VALUES (%s,%s)",(product.name,product.price)); conn.commit(); product_id=cur.lastrowid; cur.close(); conn.close(); return {"id":product_id,"name":product.name,"price":product.price}
