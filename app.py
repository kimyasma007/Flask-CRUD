from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'my key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/crud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

with app.app_context():
    db.create_all()

@app.route('/')
def Index():
    all_data = Data.query.all()
    return render_template("index.html", employees=all_data)


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        my_data = Data(name, email, phone)
        db.session.add(my_data)
        db.session.commit()

        flash("Employee Inserted Successfully")
    
    return redirect(url_for('Index'))


@app.route('/update', methods=['GET, POST'])
def update():
    if request.method == 'POST':
        # retrieve the data from the database using the id
        all_data = Data.query.get(request.form.get(id))

        # update the data
    all_data.name = request.form['name']
    all_data.email = request.form['email']
    all_data.phone = request.form['phone']

        # commit the changes to the database
    db.session.commit()
    flash("Employee Update Succesfully")

    return redirect(url_for('Index'))
if __name__ == "__main__":
    app.run(debug=True)
