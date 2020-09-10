from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, PetInfoForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route("/")
def home_page():
    """Show the home page"""
    pets = Pet.query.all()

    return render_template('home.html', pets=pets)

@app.route("/add", methods=["GET", "POST"])
def show_add_pet():
    """Renders add pet form (GET) or handles pet form submission (POST)"""
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data  
        photo_url = form.photo_url.data    
        age = form.age.data   
        notes = form.notes.data    
        flash(f"Created new pet: name is {name}, species is {species}")

        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    else: 
        return render_template('add_pet_form.html', form=form)

@app.route("/<int:petid>", methods=["GET", "POST"])
def show_pet_info(petid):
    """Show pet detail page and edit form (GET) or handles pet info edit form submission(POST)"""
    form = PetInfoForm()
    pet = Pet.query.get(petid)
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data    
        pet.notes = form.notes.data     
        pet.available = form.available.data

        db.session.add(pet)
        db.session.commit()
        flash(f"{pet.name}'s details editted")
        return redirect("/")
    else:
        form.photo_url.data = pet.photo_url
        form.notes.data = pet.notes
        form.available.data = pet.available
        return render_template("edit_pet_form.html", form=form, pet=pet)
