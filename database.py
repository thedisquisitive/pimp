from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(100))
    shortDesc = db.Column(db.String(250))
    fullDesc = db.Column(db.String(1500))

    price = db.Column(db.Double)
    cost = db.Column(db.Double)

    stock = db.Column(db.Integer)
    reorder = db.Column(db.Integer)

    def __repr__(self):
        return '<Item %r>' % self.name
    
@app.route('/')
def index():
    items = Item.query.all()
    return render_template('index.html', items=items)

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        name = request.form['name']
        shortDesc = request.form['shortDesc']
        fullDesc = request.form['fullDesc']
        price = request.form['price']
        cost = request.form['cost']
        stock = request.form['stock']
        reorder = request.form['reorder']
        db.session.add(Item(name=name, shortDesc=shortDesc, fullDesc=fullDesc, price=price, cost=cost, stock=stock, reorder=reorder))
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_item(id):
    item = Item.query.get(id)
    if request.method == 'POST':
        item.name = request.form['name']
        item.shortDesc = request.form['shortDesc']
        item.fullDesc = request.form['fullDesc']
        item.price = request.form['price']
        item.cost = request.form['cost']
        item.stock = request.form['stock']
        item.reorder = request.form['reorder']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', item=item)

@app.route('/delete/<int:id>')
def delete_item(id):
    item = Item.query.get(id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

