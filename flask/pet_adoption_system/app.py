from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)

@app.route('/')
def index():
    #show all pets
    pet_list=Pet.query.all()
    print(pet_list)
    return render_template('base.html', pet_list=pet_list)

@app.route("/add",methods=["POST"])
def add():
    #add new item
    name=request.form.get("name")
    species=request.form.get("species")
    age=request.form.get("age")

    try:
        age = int(age)  # Convert age to integer
    except ValueError:
        return redirect(url_for("index"))
    
    new_pet=Pet(name=name,species=species,age=age)
    db.session.add(new_pet)
    db.session.commit()

    # flash("Pet added successfully!", "success")
    return redirect(url_for("index"))

@app.route("/edit/<int:pet_id>", methods=["GET"])
def edit(pet_id):
    pet=Pet.query.get(pet_id)
    if not pet:
        return "Pet not found",404
    return render_template("edit_pet.html",pet=pet)



@app.route("/update/<int:pet_id>",methods=["POST"])
def update(pet_id):
    #query db:
    pet=Pet.query.get_or_404(pet_id)
    
    if pet:
        pet.name=request.form["name"]
        pet.species=request.form["species"]
        pet.age=request.form["age"]
    else:
        return "Pet not found",404

    db.session.commit()

    # flash("Pet added successfully!", "success")
    return redirect(url_for("index"))

@app.route("/delete/<int:pet_id>")
def delete(pet_id):
    pet=Pet.query.get_or_404(pet_id)
    db.session.delete(pet)
    db.session.commit()
    return redirect(url_for("index"))

    # if(pet)

# @app.route('/about')
# def about():
#     return "About"

if __name__=="__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)