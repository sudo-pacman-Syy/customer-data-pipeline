from fastapi import FastAPI, HTTPException
from database import SessionLocal, engine
from models import Customer
from ingestion import fetch_all_customers, upsert_customer

app = FastAPI()

Customer.metadata.create_all(bind=engine)


@app.post("/api/ingest")
def ingest():
    db = SessionLocal()

    try:
        data = fetch_all_customers()

        for item in data:
            upsert_customer(db, item)

        db.commit()

        return {
            "status": "success",
            "records_processed": len(data)
        }

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        db.close()


@app.get("/api/customers")
def get_customers(page: int = 1, limit: int = 10):
    db = SessionLocal()

    offset = (page - 1) * limit

    data = db.query(Customer)\
        .offset(offset)\
        .limit(limit)\
        .all()

    return data


@app.get("/api/customers/{id}")
def get_customer(id: str):
    db = SessionLocal()

    customer = db.query(Customer)\
        .filter_by(customer_id=id)\
        .first()

    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    return customer