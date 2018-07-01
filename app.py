from flask import Flask, request, redirect, render_template, session, flash, url_for
from mysqlconnection import MySQLConnector
import md5

app = Flask(__name__)
app.secret_key = "dfdfdsfsd.sdf.fsdfg.g.tedg.dt.gdf.gfd.!"
mysql = MySQLConnector(app, 'store_2')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/charts')
def charts():
    return render_template('charts.html')

@app.route('/products')
def products():
    product_query = "SELECT products.id, products.name, products.image, products.description, products.price, products.category_id FROM products;"
    products = mysql.query_db(product_query)
    return render_template('view-all-products.html', products=products)

@app.route('/add_product')
def add_product():
    return render_template('add-product.html')

@app.route('/edit_product')
def edit_product():
    return render_template('edit-product.html')

@app.route('/users')
def users():
    user_query = "SELECT * FROM users;"
    users = mysql.query_db(user_query)
    return render_template('view-all-users.html', users=users)

@app.route('/add_user')
def add_user():
    return render_template('add-user.html')

@app.route('/edit_user')
def edit_user():
    return render_template('edit-user.html')

@app.route('/orders')
def orders():
    return render_template('view-all-orders.html')

@app.route('/add_order')
def add_order():
    return render_template('add-order.html')

@app.route('/edit_order')
def edit_order():
    return render_template('edit-order.html')

@app.route('/login_now')
def login_now():
  	return render_template('login.html')

# @app.route('/register_now')
# def register_now():
#   	return render_template('register.html')


# @app.route('/register', methods=['POST'])
# def register():
#   	valid = True
#   	print request.form
# 	if request.form['email'] == "":
#   		valid = False
#   		flash("Email cannot be empty", 'danger')
# 	if request.form['name'] == "":
#   		valid = False
#   		flash("Name cannot be empty", 'danger')
# 	if request.form['password'] == "":
#   		valid = False
#     	flash("Password cannot be empty", 'danger')
# 	if request.form['password'] == request.form['confirm_password']:
#   		valid = True
# 		flash('Passwords Match!', 'success')
# 	if valid != True:
#   		return redirect('/')
# 	else:
#   		query = "INSERT INTO `login`.`users` (`email`, `password`, `name`, `created_at`, `updated_at`) VALUES (:email, :password, :name, now(), now());"
# 		data = {
# 			"email": request.form['email'],
# 			"password": md5.new(request.form['password']).hexdigest(),
# 			"name": request.form['name']
# 		}
# 		mysql.query_db(query, data)
# 		flash("Successfully Registered. Login now", 'success')
# 		return redirect(url_for('login_now'))
#   	return "got registered"


@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    valid = True
    if request.form['email'] == "":
        valid = False
        flash("Email cannot be empty", 'danger')
    if request.form['password'] == "":
        valid = False
        flash("Password cannot be empty", 'danger')
    if not valid:
        return redirect("/")
    else:
        query = "SELECT * FROM users WHERE email = :email AND password = :password"
        data = {
            "email":request.form['email'],
            "password": md5.new(request.form['password']).hexdigest()
        }
        user = mysql.query_db(query, data)
        if len(user) != 0:
            session['id'] = user[0]['id']
            session['first_name'] = user[0]['first_name']
            return redirect('/')
    return redirect('/')
	


app.run(debug=True)