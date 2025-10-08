from faker import Faker
from .database import SessionLocal, engine
from . import models

fake = Faker(["es_ES"])  # safer than es_PE

def create_schema():
    """Ensure tables exist before inserting data."""
    models.Base.metadata.create_all(bind=engine)


def seed_data():
    """Seed 500 clients with known examples at the top."""
    db = SessionLocal()
    try:
        if db.query(models.Cliente).first():
            print("Data already exists. Not seeding.")
            return

        # Known clients for API examples
        known_clients = [
            {
                "id": 100000,
                "full_name": "Ada Lovelace",
                "email": "ada@example.com",
                "dni": "12345678",
                "phone": "+51-111-222",
            },
            {
                "id": 100001,
                "full_name": "Alan Turing",
                "email": "alan@example.com",
                "dni": "87654321",
                "phone": "+51-333-444",
            },
        ]

        for k in known_clients:
            db.add(models.Cliente(**k))

        # Remaining random clients (100002–100499)
        for i in range(100002, 100500):
            cliente = models.Cliente(
                id=i,
                full_name=fake.name(),
                email=fake.email(),
                dni=fake.numerify(text="########"),
                phone=f"+51{fake.numerify(text='9########')}",
            )
            db.add(cliente)

        db.commit()
        print("✅ Seeded 500 clients (including Ada and Alan).")
    finally:
        db.close()


if __name__ == "__main__":
    create_schema()
    seed_data()
