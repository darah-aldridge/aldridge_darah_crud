from flask import render_template, request, redirect, session
from flask_app.models.user import User
from flask_app import app

@app.route("/")
def index():
    users = User.get_all()
    print(users)
    return render_template("index.html", all_users=users)

@app.route("/create_user")
def create():
    return render_template("create_user.html")

@app.route('/create_user', methods=["POST"])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"],
    }
    id = User.save(data)
    return redirect(f'/show/{id}')

@app.route('/show/<int:id>')
def show(id):
    user = User.get_one(id)
    return render_template("user.html", user=user)

@app.route('/update/<int:id>')
def update(id):
    user = User.get_one(id)
    return render_template("update_user.html", user=user)

@app.route('/update/<int:id>',methods=['POST'])
def updateUser(id):
    User.update(request.form, id)
    return redirect(f'/show/{id}')

@app.route('/delete/<int:id>')
def delete(id):
    User.delete(id)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)

