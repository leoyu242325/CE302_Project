import socket
import mysql.connector
import json
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, DateField, IntegerField
from functools import wraps
import datetime

app = Flask(__name__)

#Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123'
app.config['MYSQL_DB'] = 'retailer'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# init MYSQL

HOST = '0.0.0.0'
PORT = 9998

mysql = MySQL(app)

def myconverter(o):
	if isinstance(o, datetime.datetime):
		return o.__str__()

@app.route('/')
def index():
	return redirect(url_for('homes_retailer'))

#home page
@app.route('/home_retailer', methods=['GET', 'POST'])
def homes_retailer():
	if request.method =='POST':
		username = request.form['username']
		password_candidate = request.form['password']

		cur = mysql.connection.cursor()
		
		result = cur.execute("SELECT * FROM users WHERE username = %s", [username])

		if result > 0:

			data = cur.fetchone()
			password = data['password']

			if password_candidate == password:
				session['logged_in'] = True
				session['username'] = username

				flash('You are now logged in', 'success')
				return redirect(url_for('order_retailer'))

			else:
				error = 'Invalid login'
				return render_template('home_retailer.html',error=error)
			cur.close()
		else:
			error = 'Username not found'
			return render_template('home_retailer.html',error=error)


	return render_template('home_retailer.html')

def is_logged_in(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if "logged_in" in session:
			return f(*args, **kwargs)
		else:
			flash('Unauthorized, Please login','danger')
			return redirect(url_for('home_retailer'))
	return wrap

class Order_and_Delivery_infor(Form):
	name = StringField('Name')
	phone_number = StringField('Phone Number')
	email_address = StringField('Email Address')
	address = StringField('Address')
	quantity= IntegerField('Quantity')
	price= IntegerField('Price')
	weight= IntegerField('Weight')


class Searching(Form):
	search_tracking= StringField('Tracking No')
	search_order= StringField('Order No')


@app.route('/order_retailer', methods=['GET','POST'])
@is_logged_in
def order_retailer():

	form = Searching(request.form)
	
	if request.method == 'POST':


		search_order = request.form['search_order']

		if search_order == "":

			cur = mysql.connection.cursor()

			result = cur.execute("SELECT Order_No, Date, Customer_ID, Name, Phone_Number, Email, Address, order_item_no, Type, Item_Name, Quantity, Price,Weight FROM order_form") 

			order_infor =cur.fetchall()

			if result > 0:
				return render_template('order_retailer.html', order_infor=order_infor, form=form)

			else:
				msg = 'No order information found'
				return render_template('order_retailer.html', msg = msg, form=form)

			cur.close()

		else:
			cur = mysql.connection.cursor()

			result = cur.execute("SELECT Order_No, Date, Customer_ID, Name, Phone_Number, Email, Address, order_item_no, Type, Item_Name, Quantity, Price,Weight FROM order_form WHERE Order_No =%s", [search_order])

			order_infor = cur.fetchall()

			if result > 0:
				return render_template('order_retailer.html', order_infor=order_infor, form=form)

			else:
				msg = 'No order information found'
				return render_template('order_retailer.html', msg = msg, form=form)

			cur.close()

	else:

		cur = mysql.connection.cursor()

		result = cur.execute("SELECT Order_No, Date, Customer_ID, Name, Phone_Number, Email, Address, order_item_no, Type, Item_Name, Quantity, Price,Weight FROM order_form") 

		order_infor =cur.fetchall()

		if result > 0:
			return render_template('order_retailer.html', order_infor=order_infor, form=form)

		else:
			msg = 'No order information found'
			return render_template('order_retailer.html', msg = msg, form =form)

		cur.close()

	return render_template('order_retailer.html', form=form)


@app.route('/delivery_retailer', methods=['GET','POST'])
@is_logged_in
def delivery_retailer():

	form = Searching(request.form)

	
	if request.method == 'POST':

		search_tracking = request.form['search_tracking']

		if search_tracking == "":
			
			cur = mysql.connection.cursor()

			result = cur.execute("SELECT order_form.Order_No,delivery_form.tracking_no,delivery_form.delivery_price,delivery_form.estimated_date FROM order_form INNER JOIN delivery_form ON order_form.order_item_no = delivery_form.order_item_no")  
		
			delivery_infor =cur.fetchall()

			if result > 0:
				return render_template('delivery_retailer.html', delivery_infor=delivery_infor, form=form)

			else:
				msg = 'No delivery information found'
				return render_template('delivery_retailer.html', msg = msg, form=form)

			cur.close()

		else:

			cur = mysql.connection.cursor()

			result = cur.execute("SELECT order_form.Order_No,delivery_form.tracking_no,delivery_form.delivery_price,delivery_form.estimated_date FROM order_form INNER JOIN delivery_form ON order_form.order_item_no = delivery_form.order_item_no WHERE delivery_form.tracking_no = %s", [search_tracking])

			delivery_infor = cur.fetchall()

			if result > 0:
				return render_template('delivery_retailer.html', delivery_infor=delivery_infor, form=form)

			else:
				msg = 'No delivery information found'
				return render_template('delivery_retailer.html', msg = msg, form=form)

			cur.close()


	else:
		cur = mysql.connection.cursor()

		result = cur.execute("SELECT order_form.Order_No,delivery_form.tracking_no,delivery_form.delivery_price,delivery_form.estimated_date FROM order_form INNER JOIN delivery_form ON order_form.order_item_no = delivery_form.order_item_no")  

		delivery_infor =cur.fetchall()

		if result > 0:
			return render_template('delivery_retailer.html', delivery_infor=delivery_infor, form=form)

		else:
			msg = 'No delivery information found'
			return render_template('delivery_retailer.html', msg = msg, form=form)

		cur.close()

	return render_template('delivery_retailer.html', form = form)


@app.route('/edit_order_retailer/<string:order_item_no>',methods=['GET', 'POST'])
@is_logged_in
def edit_order_retailer(order_item_no):
	cur = mysql.connection.cursor()

	cur.execute("SELECT * FROM order_form WHERE order_item_no = %s", [order_item_no])

	order_infor = cur.fetchone()
	cur.close()

	form = Order_and_Delivery_infor(request.form)

	form.name.data = order_infor['Name']
	form.phone_number.data = order_infor['Phone_Number']
	form.email_address.data = order_infor['Email']
	form.address.data = order_infor['Address']
	form.quantity.data = order_infor['Quantity']
	form.price.data = order_infor['Price']
	form.weight.data = order_infor['Weight']
	order_item_no = order_infor['order_item_no']
	order_no = order_infor['Order_No']

	if request.method == 'POST':
		name = request.form['name']
		phone_number = request.form['phone_number']
		email_address = request.form['email_address']
		address = request.form['address']
		quantity = request.form['quantity']
		price = request.form['price']
		weight = request.form['weight']


		cur = mysql.connection.cursor()
		cur.execute("UPDATE order_form SET Name = %s, Phone_Number = %s, Email = %s, Address = %s, Quantity = %s, Price = %s, Weight = %s WHERE Order_No = %s and order_item_no=%s", (name, phone_number,email_address,address,quantity,price,weight,order_no,order_item_no))
		mysql.connection.commit()

		cur.close()

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((HOST, PORT))

		while True:
			signo = "edit"
			infor = signo, name, phone_number,email_address,address,quantity,weight,order_no,order_item_no
			json_result= json.dumps(infor)
			s.send(json_result)
			data = s.recv(1024)
		
			print(data)
			s.close()

		flash('Delivery Record Updated', 'success')

		return redirect(url_for('order_retailer'))

	return render_template('edit_order_retailer.html',form=form, order_infor=order_infor)

@app.route('/delete_delivery/<string:order_item_no>',methods = ['POST'])
@is_logged_in
def delete_order_retailer(order_item_no):
	cur = mysql.connection.cursor()
	cur.execute("SELECT * FROM order_form WHERE order_item_no = %s", [order_item_no])
	delivery_infor = cur.fetchone()
	order_no = delivery_infor['Order_No']
	cur.execute("DELETE FROM order_form WHERE order_item_no=%s ", [order_item_no])
	cur.execute("DELETE FROM delivery_form WHERE order_item_no=%s ",[order_item_no])

	mysql.connection.commit()

	cur.close()

	order_item_no = delivery_infor['order_item_no']
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))

	while True:
		signo = "delete"
		infor = signo,order_no,order_item_no
		json_result= json.dumps(infor)
		s.send(json_result)
		data = s.recv(1024)
		print(data)
		s.close()
	flash('Delivery information deleted', 'success')

	return redirect(url_for('delivery'))

@app.route('/logout')
def logout():
	session.clear()
	flash('You are now logged out', 'success')
	return redirect(url_for('homes_retailer'))



if __name__ == '__main__':
	app.secret_key='secret123'
	app.run(debug=True)