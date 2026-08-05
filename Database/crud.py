from main import app,db, Puppy

#CREATE
with app.app_context():
    my_puppy = Puppy("Z", 13)
    db.session.add(my_puppy)
    db.session.commit()


#READ
    all_puppies=Puppy.query.all()
    print(all_puppies)

#SELECT BY ID
    puppy_1 = db.session.get(Puppy,1)
    print(puppy_1)

#Filters
    puppy_z = Puppy.query.filter_by(name="Z").all()
    print(puppy_z)

#Update
    first_puppy = puppy_1 = db.session.get(Puppy,2)
    first_puppy.age = 10
    db.session.add(first_puppy)
    db.session.commit()

#DELETE
    z_pup=Puppy.query.filter_by(name="Z").all()

    for pup in z_pup:
        db.session.delete(pup)

    del_puppy_1 = db.session.get(Puppy, 1)
    db.session.delete(del_puppy_1)

    db.session.commit()


