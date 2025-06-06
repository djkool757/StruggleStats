import json
from backend.app import create_app
from app.models import db, Category, Subtopic, Concept 

app = create_app()


with app.app_context():
    with open("aamc_mcat_outline_parsed.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    for category_data in data:
        category = Category(name=category_data["category"])
        db.session.add(category)
        db.session.flush()  # Populate category.id

        for sub in category_data.get("subtopics", []):
            subtopic = Subtopic(title=sub["title"], category_id=category.id)
            db.session.add(subtopic)
            db.session.flush()

            for concept in sub.get("concepts", []):
                c = Concept(description=concept, subtopic_id=subtopic.id)
                db.session.add(c)

    db.session.commit()
    print("✅ MCAT data seeded into the database.")
