from models import db, Puppy, Owner, Toy, app

fido = Puppy("Fido")
z = Puppy("Z")


with app.app_context():
    db.session.add_all([fido, z])
    db.session.commit()

    all_puppies=Puppy.query.all()
    print(all_puppies)


    z = Puppy.query.filter_by(name="Z").first()

    #create owner
    jomir = Owner("Jomir", z.id)

    toy1 = Toy("Chew Toy", z.id)
    toy2 = Toy("ball",z.id)

    db.session.add_all([jomir, toy1, toy2])
    db.session.commit()

    z = Puppy.query.filter_by(name="Z").first()

    print(z.report_toys())