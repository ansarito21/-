from flask import Flask, render_template, request, redirect, url_for, session
import uuid

app = Flask(__name__)
app.secret_key = 'supersecretkey'

USERS = {}
TICKETS = [
    {"id": 1, "name": "Детский билет", "price": 2500, "description": "Для детей от 3 до 12 лет.", "image": "child_ticket.jpg"},
    {"id": 2, "name": "Взрослый билет", "price": 5000, "description": "Для посетителей старше 12 лет.", "image": "adult_ticket.jpg"},
    {"id": 3, "name": "Семейный билет", "price": 7500, "description": "На 2 взрослых и 2 детей.", "image": "family_ticket.jpg"},
    {"id": 4, "name": "VIP билет", "price": 25000, "description": "С доступом в VIP-зону и бесплатными напитками.", "image": "vip_ticket.jpg"},
    {"id": 5, "name": "Групповой билет", "price": 20000, "description": "Для группы до 5 человек. Исключительно для взрослых.", "image": "group_ticket.jpg"},
    {"id": 6, "name": "Выходной билет", "price": 7500, "description": "Для посещения аквапарка только в выходные дни", "image": "weekend_ticket.jpg"}
]
ORDERS = []
cart = []

@app.route('/')
def home():
    return render_template('home.html', tickets=TICKETS, user=session.get('user'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in USERS:
            error_message = "Пользователь уже существует!"
            return render_template('register.html', error_message=error_message)
        USERS[username] = password
        session['user'] = username
        return redirect(url_for('home'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if USERS.get(username) == password:
            session['user'] = username
            return redirect(url_for('home'))
        error_message = "Неверное имя пользователя или пароль!"
        return render_template('login.html', error_message=error_message)
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

@app.route('/add_to_cart/<int:ticket_id>', methods=['POST'])
def add_to_cart(ticket_id):
    quantity = int(request.form.get('quantity', 1))
    date = request.form.get('date')
    time = request.form.get('time')
    ticket = next((ticket for ticket in TICKETS if ticket['id'] == ticket_id), None)
    if ticket:
        cart.append({
            'ticket': ticket,
            'quantity': quantity,
            'date': date,
            'time': time
        })
    return render_template('home.html', tickets=TICKETS, user=session.get('user'), success_message="Билет добавлен в корзину!")

@app.route('/remove_from_cart/<int:ticket_id>', methods=['POST'])
def remove_from_cart(ticket_id):
    global cart
    cart = [item for item in cart if item['ticket']['id'] != ticket_id]
    return redirect(url_for('view_cart'))

@app.route('/update_quantity/<int:ticket_id>', methods=['POST'])
def update_quantity(ticket_id):
    quantity = int(request.form.get('quantity', 1))
    global cart
    for item in cart:
        if item['ticket']['id'] == ticket_id:
            item['quantity'] = quantity
            break
    return redirect(url_for('view_cart'))

@app.route('/cart')
def view_cart():
    total = sum(item['ticket']['price'] * item['quantity'] for item in cart)
    return render_template('cart.html', cart=cart, total=total)

@app.route('/checkout', methods=['POST'])
def checkout():
    if not session.get('user'):
        return redirect(url_for('login'))

    if cart:
        order_id = str(uuid.uuid4())
        ORDERS.append({"user": session['user'], "order_id": order_id, "tickets": cart.copy()})
        cart.clear()
        return render_template('success.html', order_id=order_id)
    return "Ваша корзина пуста!"

@app.route('/admin')
def admin_panel():
    if session.get('user') != 'admin':
        return redirect(url_for('home'))
    return render_template('admin.html', orders=ORDERS)

@app.route('/delete_order/<order_id>', methods=['POST'])
def delete_order(order_id):
    global ORDERS
    ORDERS = [order for order in ORDERS if order['order_id'] != order_id]
    return redirect(url_for('admin_panel'))

if __name__ == '__main__':
    app.run(debug=True)
