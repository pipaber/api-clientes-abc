from faker import Faker
from .database import SessionLocal, engine
from . import models

fake = Faker(["es_ES"])  # use a stable Spanish locale available in Faker

def create_schema():
    """Ensure tables exist before inserting data."""
    models.Base.metadata.create_all(bind=engine)

def seed_data():
    """Seed 500 clients with IDs from 100000 to 100499."""
    db = SessionLocal()
    try:
        if db.query(models.Cliente).first():
            print("Data already exists. Not seeding.")
            return

        for i in range(500):
            cliente = models.Cliente(
                id=100000 + i,
                full_name=fake.name(),
                email=fake.email(),
                dni=fake.numerify(text="########"),
                phone=f"+51{fake.numerify(text='9########')}",
            )
            db.add(cliente)

        db.commit()
        print("✅ Seeded 500 clients (100000–100499).")
    finally:
        db.close()

if __name__ == "__main__":
    create_schema()
    seed_data()
