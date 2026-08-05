from main import app,db, Puppy

#creates all teh tables Model --> Db Table
with app.app_context():
    db.create_all()

    sam = Puppy("Sammy",3)
    frank = Puppy("Frankie",4)

    db.session.add_all([sam,frank])

    db.session.commit()

    print(sam.id)