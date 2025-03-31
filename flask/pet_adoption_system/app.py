from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY']="abcd1234"

db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view="login"

class User(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(80),unique=True,nullable=False)
    password=db.Column(db.String(300), nullable=False)

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/auth/signup', methods=["GET","POST"])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        print(f"Signup attempt - Username: {username}, Password: {password}")  # Debug print

        if User.query.filter_by(username=username).first():
            return redirect(url_for('signup'))
        
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/auth/login', methods=["GET","POST"])
def login():
    if request.method=="POST":
        username=request.form["username"]
        password=request.form["password"]

        print(f"Login attempt - Username: {username}, Password: {password}")  #Debug

        user=User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password,password):
            login_user(user)
            return redirect(url_for('index'))
        
    return render_template('login.html')

@app.route('/auth/logout', methods=["POST","GET"])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/')
@login_required
def index():
    #show all pets
    pet_list=Pet.query.all()
    print("Fetched Pets:", pet_list)
    return render_template('dashboard.html', pet_list=pet_list)
        

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