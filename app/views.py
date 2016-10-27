from flask import render_template, redirect, request
from app import app, models
# from models import *
from .forms import LoginForm,AddTripForm
# Access the models file to use SQL functions
from flask import session

@app.route('/')
def index():
    return redirect('/login')
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')
@app.route('/login', methods=['GET', 'POST'])
def login():
    #form = LoginForm()
    if request.method=='POST':
        password = request.form["password"]
        username = request.form["username"]
        login = models.retrieve_password(username)
        if login[0][0] == password:
            session['uname']=username
            return redirect('/trips')
        return render_template('login.html')    
    return render_template('login.html') 

@app.route('/trips')
def trips():
        if session.get("uname") is None:
            return redirect('/login')
        trips = models.retrieve_trips(session['uname'])
        print (trips)
        return render_template('trips.html',trips=trips)
    
@app.route('/add_trip' ,methods =['GET','POST'])
def add_trips():
    if session.get("uname") is None:
            return redirect('/login')
    form = AddTripForm()
    result = models.retrieve_friends(session["uname"])
    friends =[]
    for r in result:
        friends.append((r[0],r[0]))
    form.friend.choices=friends
   
    if (form.validate_on_submit()):
        friend = form.friend.data
        destination= form.destination.data
        trip_name=form.trip_name.data
        models.add_trip(session["uname"],friend,destination,trip_name)
        return redirect("/trips")

    return render_template('trip.html',trips=trips,form =form)
@app.route('/delete_trip<int:value>' ,methods =['GET','POST'])
def delete_trip(value):
    if session.get("uname") is None:
            return redirect('/login')
    models.delete_trip(value)
    
    return redirect("/trips")
    
# @app.route('/create_customer', methods=['GET', 'POST'])
# def create_customer():
#     form = CustomerForm()
#     if form.validate_on_submit():
#         first_name = form.first_name.data,
#         last_name = form.last_name.data,
#         company = form.company.data,
#         email = form.email.data,
#         phone = form.phone.data,
#         street_address = form.street_address.data,
#         city = form.city.data,
#         state = form.state.data,
#         country = form.country.data,
#         zipcode = form.zipcode.data
#         models.insert_customer(company, email, first_name, last_name, phone, street_address, city, state, country, zipcode)
#         return redirect('/customers')
#     return render_template('customer.html', form=form)

# @app.route('/customers')
# def display_customer():
#     customers = models.retrieve_customers()
#     orders = models.retrieve_orders()
#     return render_template('home.html',
#                             customers=customers,orders=orders)

# @app.route('/create_order<int:value>', methods=['GET', 'POST'])
# def create_order(value):
#     form = OrdersForm()
#     if form.validate_on_submit():
#         name_of_part = form.name_of_part.data,
#         manufacturer_of_part = form.manufacturer_of_part.data
#         customer_id = value
#         models.insert_order(name_of_part,manufacturer_of_part,customer_id)
#         return redirect('/customers')
#     return render_template('order.html', form=form)

# @app.route('/orders')
# def display_order():
#     customers = models.retrieve_customers()
#      orders = models.retrieve_orders()
#      return render_template('order.html',
#                              customers=customers)