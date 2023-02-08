from contextlib import _RedirectStream
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] =  'mysql+pymysql://root:@localhost/CSM'
db = SQLAlchemy(app)

class Message_list(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(20),nullable=False)
    contact=db.Column(db.String(12),nullable=False)
    message=db.Column(db.String,nullable=False)

class Storage_list(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50), nullable=False)
    cost=db.Column(db.Float)
    description=db.Column(db.String)
    Capacity=db.Column(db.Integer)
    status=db.Column(db.String)

class Admin(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(50), nullable=False)
    password=db.Column(db.String(50), nullable=False)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(50), nullable=False)
    password=db.Column(db.String(50), nullable=False)
    
class Booking_details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50), nullable=False)
    gender=db.Column(db.String)
    email=db.Column(db.String(20),nullable=False)
    number=db.Column(db.String(50),nullable=False)
    username=db.Column(db.String(50), nullable=False)
    password=db.Column(db.String(50), nullable=False)
    storage_type=db.Column(db.Integer,nullable=False)
    No_of_storages=db.Column(db.Integer,nullable=False)
    date_from=db.Column(db.String,nullable=False)
    date_to=db.Column(db.String,nullable=False)
    No_of_days=db.Column(db.Integer)
    address=db.Column(db.String(50), nullable=False)
    city=db.Column(db.String(20), nullable=False)
    state=db.Column(db.String(20), nullable=False)
    pincode=db.Column(db.Integer, nullable=False)


class Booking_list(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_code=db.Column(db.String(50),nullable=True)
    client_name=db.Column(db.String(50), nullable=False)
    sex=db.Column(db.String)
    email=db.Column(db.String(20),nullable=False)
    Phone=db.Column(db.String(50),nullable=False)
    storage_id=db.Column(db.Integer)
    No_of_storages=db.Column(db.Integer,nullable=False)
    date_from=db.Column(db.String,nullable=True)
    date_to=db.Column(db.String,nullable=True)
    No_of_days=db.Column(db.Integer)
    amount=db.Column(db.Float)
    address=db.Column(db.String(50), nullable=False)
    city=db.Column(db.String(20), nullable=False)
    state=db.Column(db.String(20), nullable=False)
    pincode=db.Column(db.Integer, nullable=False)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/team")
def team():
    return render_template('team.html')

@app.route("/storages")
def storages():
    return render_template('storages.html')

@app.route("/more")
def more():
    return render_template('more.html')

@app.route("/booking", methods=['GET','POST'])
def booking():
    if(request.method=='POST'):
        name=request.form.get('name')
        gender=request.form.get('gender')
        email=request.form.get('email')
        number=request.form.get('number')
        username=request.form.get('username')
        password=request.form.get('password')
        storage_type=request.form.get('storage_type')
        No_of_storages=request.form.get('No_of_storages')
        date_from=request.form.get('date_from')
        date_to=request.form.get('date_to')
        No_of_days=request.form.get('No_of_days')
        address=request.form.get('address')
        city=request.form.get('city')
        state=request.form.get('state')
        pincode=request.form.get('pincode')

        entry=Booking_details(name=name,gender=gender,email=email,number=number,username=username,password=password,storage_type=storage_type,No_of_storages=No_of_storages, date_from=date_from,date_to=date_to,No_of_days=No_of_days, address=address,city=city,state=state,pincode=pincode)
        db.session.add(entry)
        db.session.commit()
        return render_template('confirm.html')
    return render_template('booking.html')

@app.route("/contact", methods=['GET','POST'])
def contact():
    if(request.method=='POST'):
        name=request.form.get('name')
        email=request.form.get('email')
        message=request.form.get('message')
        phone=request.form.get('phone')
        
        
        entry=Message_list(fullname=name,email=email,message=message,contact=phone)
        db.session.add(entry)
        db.session.commit()
        return render_template('msg.html')

    return render_template('contact.html')

@app.route("/confirm")
def confirm():
    return render_template('confirm.html')

@app.route("/admin", methods=['GET','POST'])
def admin():
    if request.method == 'POST':
        username=request.form.get('username')
        password=request.form.get('password')
        user=Admin.query.filter_by(username=username).first()
        userpass=Admin.query.filter_by(password=password).first()
        if user and userpass:
            return render_template('adminred.html')
        else:
            return "Invalid username or password"
    return render_template('admin.html')
    
@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username=request.form.get('username')
        password=request.form.get('password')
        user=Users.query.filter_by(username=username).first()
        userpass=Users.query.filter_by(password=password).first()
        if user and userpass:
            return render_template('user.html')
        else:
            return "Invalid username or password"
    return render_template('login.html')
        
@app.route("/booking_details", methods=['GET','POST'])
def booking_details():
     booking_details=Booking_details.query.all()
     return render_template('booking_details.html',booking_details=booking_details)    

@app.route("/booking_list", methods=['GET','POST'])
def booking_list():
    booking_list=Booking_list.query.all()
    return render_template('booking_list.html',booking_list=booking_list) 

@app.route("/storage_list", methods=['GET','POST'])
def storage_list():
    storage_list=Storage_list.query.all()
    return render_template('storage_list.html',storage_list=storage_list)    

@app.route("/message_details", methods=['GET','POST'])
def message_details():
    message_details=Message_list.query.all()
    return render_template('message_details.html',message_list=message_details)    

@app.route("/msg")
def msg():
    return render_template('msg.html')

@app.route("/adminred")
def adminred():
    return render_template('adminred.html')

@app.route("/delete/<string:id>", methods=['GET','POST'])
def delete(id):
    booking_list=Booking_list.query.filter_by(id=id).first() 
    db.session.delete(booking_list)
    db.session.commit()
    return  "Successfully Deleted"



app.run(debug=True)