from market import app, db
# from market.models import Item
from market.models import User

with app.app_context():
    db.drop_all()
    db.create_all()
    print("Tables reset.")

    # Optional: Add seed data
    u1 = User(username="user1",password_hash='12365',email_address='pl@yahoo.com')
    u2 = User(username="user2",password_hash='12789',email_address='pl@mi.com')
    db.session.add(u1)
    db.session.add(u2)
    db.session.commit()

   
