from market import app, db
# from market import Item
from market.models import Item


with app.app_context():
    db.create_all()
    print("Database tables created.")

with app.app_context():
    # Check if items exist before adding
    if not Item.query.filter_by(description="desc").first():
        item1 = Item(name="iphone10", price=500, barcode='236547563498', description='desc')
        db.session.add(item1)

    if not Item.query.filter_by(description="desc2").first():
        item2 = Item(name="phone13", price=5000, barcode='236786349845', description='desc2')
        db.session.add(item2)

    db.session.commit()
