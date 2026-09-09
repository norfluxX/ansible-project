import os
from fastapi import FastAPI
import mysql.connector

app = FastAPI(title="Product Service")


def db():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "mysql"),
        database=os.getenv("MYSQL_DATABASE", "ecommerce"),
        user=os.getenv("MYSQL_USER", "app"),
        password=os.getenv("MYSQL_PASSWORD", "app_password"),
    )


@app.get("/health")
def health():
    return {"service": "product-service", "status": "ok"}


@app.get("/products")
def products():
    conn = db()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT id, name, price FROM products")
    rows = cur.fetchall()
    cur.close(); conn.close()
    return rows
