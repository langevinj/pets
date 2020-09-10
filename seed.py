from models import Pet, db
from app import app

db.drop_all()
db.create_all()

Pet.query.delete()

#Create some example pets

lucky = Pet(name="Lucky", species="Dog",
            photo_url="https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/American_Eskimo_Dog.jpg/1527px-American_Eskimo_Dog.jpg",
            age=12,
            available=True)

bart = Pet(name="Bart", species="Parrot",
           photo_url="https://images.all-free-download.com/images/graphiclarge/parrot_bird_ara_218995.jpg",
           available=False)

yams = Pet(name="Yams", species="Cat")

#add pets to session
db.session.add(lucky)
db.session.add(bart)
db.session.add(yams)

#commit to db
db.session.commit()
