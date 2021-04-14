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
app.config['MYSQL_DB'] = 'logistic'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# init MYSQL

HOST = '0.0.0.0'
PORT = 9999

mysql = MySQL(app)

def myconverter(o):
	if isinstance(o, datetime.datetime):
		return o.__str__()

@app.route('/')
def index():
	return redirect(url_for('homes'))

#home page
@app.route('/home', methods=['GET', 'POST'])
def homes():
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
				return redirect(url_for('delivery'))

			else:
				error = 'Invalid login'
				return render_template('home.html',error=error)
			cur.close()
		else:
			error = 'Username not found'
			return render_template('home.html',error=error)


	return render_template('home.html')

def is_logged_in(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if "logged_in" in session:
			return f(*args, **kwargs)
		else:
			flash('Unauthorized, Please login','danger')
			return redirect(url_for('homes'))
	return wrap

class Order_and_Delivery_infor(Form):
	Delivery_Price= IntegerField('Delivery Price', [validators.required()])
	Estimated_Date= DateField('Estimated Date', format = '%Y-%m-%d')


class Searching(Form):
	search_tracking= StringField('Tracking No')
	search_order= StringField('Order No')


@app.route('/order', methods=['GET','POST'])
@is_logged_in
def order():
	form = Searching(request.form)
	
	if request.method == 'POST':


		search_order = request.form['search_order']

		if search_order == "":
			cur = mysql.connection.cursor()

			result = cur.execute("SELECT * FROM orders") 

			order_infor =cur.fetchall()

			if result > 0:
				return render_template('order.html', order_infor=order_infor, form=form)

			else:
				msg = 'No order information found'
				return render_template('order.html', msg = msg, form=form)

			cur.close()

		else:

			cur = mysql.connection.cursor()

			result = cur.execute("SELECT * FROM orders WHERE order_no =%s", [search_order])

			order_infor = cur.fetchall()

			if result > 0:
				return render_template('order.html', order_infor=order_infor, form=form)

			else:
				msg = 'No order information found'
				return render_template('order.html', msg = msg, form=form)

			cur.close()

	else:
		cur = mysql.connection.cursor()

		result = cur.execute("SELECT * FROM orders") 

		order_infor =cur.fetchall()

		if result > 0:
			return render_template('order.html', order_infor=order_infor, form=form)

		else:
			msg = 'No order information found'
			return render_template('order.html', msg = msg, form =form)

		cur.close()

	return render_template('order.html', form=form)


@app.route('/delivery', methods=['GET','POST'])
@is_logged_in
def delivery():


	form = Searching(request.form)

	
	if request.method == 'POST':


		search_tracking = request.form['search_tracking']

		if search_tracking == "":
			cur = mysql.connection.cursor()

			result = cur.execute("SELECT delivery.order_no, delivery.tracking_no, orders.Name, orders.Phone_Number, orders.Email_Address, orders.Address, delivery.delivery_price, delivery.estimated_delivery_date, delivery.order_item_no FROM orders INNER JOIN delivery ON orders.order_item_no=delivery.order_item_no") 

			delivery_infor =cur.fetchall()

			if result > 0:
				return render_template('delivery.html', delivery_infor=delivery_infor, form=form)

			else:
				msg = 'No delivery information found'
				return render_template('delivery.html', msg = msg, form=form)

			cur.close()

		else:

			cur = mysql.connection.cursor()

			result = cur.execute("SELECT delivery.order_no, delivery.tracking_no, orders.Name, orders.Phone_Number, orders.Email_Address, orders.Address, delivery.delivery_price, delivery.estimated_delivery_date, delivery.order_item_no FROM orders INNER JOIN delivery ON orders.order_item_no=delivery.order_item_no WHERE delivery.tracking_no = %s", [search_tracking])

			delivery_infor = cur.fetchall()

			if result > 0:
				return render_template('delivery.html', delivery_infor=delivery_infor, form=form)

			else:
				msg = 'No delivery information found'
				return render_template('delivery.html', msg = msg, form=form)

			cur.close()


	else:
		cur = mysql.connection.cursor()

		result = cur.execute("SELECT delivery.order_no, delivery.tracking_no, orders.Name, orders.Phone_Number, orders.Email_Address, orders.Address, delivery.delivery_price, delivery.estimated_delivery_date, delivery.order_item_no FROM orders INNER JOIN delivery ON orders.order_item_no=delivery.order_item_no") 

		delivery_infor =cur.fetchall()

		if result > 0:
			return render_template('delivery.html', delivery_infor=delivery_infor, form=form)

		else:
			msg = 'No delivery information found'
			return render_template('delivery.html', msg = msg, form=form)

		cur.close()

	return render_template('delivery.html', form = form)

@app.route('/edit_delivery/<string:tracking_no>',methods=['GET', 'POST'])
@is_logged_in
def edit_delivery(tracking_no):
	cur = mysql.connection.cursor()

	cur.execute("SELECT * FROM delivery WHERE tracking_no = %s", [tracking_no])

	delivery_infor = cur.fetchone()
	cur.close()

	form = Order_and_Delivery_infor(request.form)

	form.Delivery_Price.data = delivery_infor['delivery_price']
	form.Estimated_Date.data = delivery_infor['estimated_delivery_date']
	order_no = delivery_infor['order_no']


	if request.method == 'POST':
		delivery_price = request.form['Delivery_Price']
		estimated_date = request.form['Estimated_Date']

		cur = mysql.connection.cursor()
		cur.execute("UPDATE delivery SET delivery_price = %s, estimated_delivery_date = %s WHERE tracking_no = %s", (delivery_price, estimated_date, tracking_no))

		mysql.connection.commit()

		cur.close()

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((HOST, PORT))

		while True:
			signo = "edit"
			infor = signo,delivery_price,estimated_date,tracking_no
			json_result= json.dumps(infor)
			s.send(json_result)
			data = s.recv(1024)
			print(data)
			s.close()

		flash('Delivery Record Updated', 'success')

		return redirect(url_for('delivery'))

	return render_template('edit_delivery.html',form=form, delivery=delivery, delivery_infor=delivery_infor)

@app.route('/delete_delivery/<string:order_item_no>',methods = ['POST'])
@is_logged_in
def delete_delivery(order_item_no):
	cur = mysql.connection.cursor()
	cur.execute("SELECT * FROM delivery WHERE order_item_no=%s", [order_item_no])
	delivery_infor = cur.fetchone()

	tracking_no = delivery_infor['tracking_no']
	order_item_no = delivery_infor['order_item_no']
	cur.execute("DELETE FROM delivery WHERE order_item_no = %s ", [order_item_no])

	mysql.connection.commit()

	cur.close()

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))

	while True:
		signo = "delete"
		infor = signo,tracking_no,order_item_no
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
	return redirect(url_for('homes'))



if __name__ == '__main__':
	app.secret_key='secret123'
	app.run(debug=True)