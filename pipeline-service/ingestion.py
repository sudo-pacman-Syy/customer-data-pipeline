import requests
from sqlalchemy.orm import Session
from models import Customer

BASE_URL = "http://mock-server:5000/api/customers"


def fetch_all_customers():
    page = 1
    all_data = []

    while True:
        res = requests.get(f"{BASE_URL}?page={page}")
        result = res.json()
        
        data = result["data"]

        if not data:
            break

        all_data.extend(data)
        page += 1

    return all_data


def upsert_customer(db: Session, data):
    existing = db.query(Customer).filter_by(
        customer_id=data["customer_id"]
    ).first()

    if existing:
        for key, value in data.items():
            setattr(existing, key, value)
    else:
        db.add(Customer(**data))