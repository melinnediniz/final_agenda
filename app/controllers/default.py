from flask import render_template, request, redirect, url_for, current_app
from app import app, db
from app.models.tables.user import User


@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login",methods=["GET", "POST"])
def login():
    value = ""
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
 
        login = User.query.filter_by(email=email, password=password).first()
        print(f"=========== LOGIN: {login}")
        if login is not None:
            response = current_app.make_response(render_template("homepage.html"))
            response.set_cookie('authUser', str(login))
            return response
        else:
            return "Usuário não existe"
    
    return render_template("login.html")


@app.route("/signup", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        try:
            new_user = User(username,email,password, name)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("sign_up"))
        except Exception as e:
            return f"{e}"
        
    return render_template("register.html") 

@app.route("/homepage")
def homepage():
    return render_template('homepage.html')

     # db.session.add(User)
     # db.session.commit()

#@app.route("/ola", defaults={'name': None})
#@app.route("/ola/<name>")
#def teste(name):
#    if name:
#        return "olá, %s!" % name
#    else:
#        return "ola, usuário!"
    
#@app.route("/usuario/<int:id>")
#def user(id):
#    return f"ID: {id}"