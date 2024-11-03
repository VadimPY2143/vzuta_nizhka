from flask import Flask, render_template, request, abort, url_for, redirect
from db import order_table, engine
from sqlalchemy import insert, select, update, delete, func
from sqlalchemy.orm import Session

app = Flask(__name__)

shoes = {
    "id": [],
    "name": [],
    "price": [],
    "description": [],
    "type": [],
    "photo": []
}


with Session(engine) as session:
    stmt = select(order_table)
    results = session.execute(stmt).fetchall()
    for row in results:
        shoes["id"].append(row.id)
        shoes["name"].append(row.name)
        shoes["price"].append(row.price)
        shoes["description"].append(row.description)
        shoes["type"].append(row.type)
        shoes["photo"].append(row.picture)

@app.route('/')
def main():
    with Session(engine) as session:
        stmt = select(func.max(order_table.c.id))
        length = session.execute(stmt).scalar()
    return render_template('index.html', shoes=shoes, length=length)


@app.route('/add', methods=['GET', 'POST'])
def add_model():
    with Session(engine) as session:
        stmt = select(func.max(order_table.c.id))
        length = session.execute(stmt).scalar()

    if request.method == 'POST':
        with Session(engine) as session:
            stmt = insert(order_table).values(
                name=request.form['name'],
                price=request.form['price'],
                description=request.form['description'],
                type=request.form['category'],
                picture=request.files['photo'].read()
            )
            session.execute(stmt)
            session.commit()

        return render_template("index.html", length=length, shoes=shoes)

    return render_template('add_model_form.html')



@app.route('/flipflops')
def flipflops():
    with Session(engine) as session:
        stmt = select(func.max(order_table.c.id))
        length = session.execute(stmt).scalar()
    return render_template('flipflops.html', length=length, shoes=shoes)


@app.route('/loafers')
def loafers():
    with Session(engine) as session:
        stmt = select(func.max(order_table.c.id))
        length = session.execute(stmt).scalar()
    return render_template('loafers.html', length=length, shoes=shoes)


@app.route('/sandals')
def sandals():
    with Session(engine) as session:
        stmt = select(func.max(order_table.c.id))
        length = session.execute(stmt).scalar()
    return render_template('sandals.html', length=length, shoes=shoes)



@app.route('/slipons')
def slipons():
    with Session(engine) as session:
        stmt = select(func.max(order_table.c.id))
        length = session.execute(stmt).scalar()
    return render_template('slipons.html', length=length, shoes=shoes)


@app.route('/sneakers')
def sneakers():
    with Session(engine) as session:
        stmt = select(func.max(order_table.c.id))
        length = session.execute(stmt).scalar()
    return render_template('sneakers.html', length=length, shoes=shoes)


@app.route('/shoe')
def shoe():
    with Session(engine) as session:
        stmt = select(func.max(order_table.c.id))
        length = session.execute(stmt).scalar()
    return render_template('shoe.html', length=length, shoes = shoes)


@app.route(f'/models/<int:model_id>/')
def models(model_id):
    model = get_models(model_id)
    return render_template('models.html', model=model, )


def get_models(model_id):
    with Session(engine) as session:
        stmt = select(order_table).where(order_table.c.id == model_id + 1)
        post = session.execute(stmt).fetchone()

        if post is None:
            abort(404)

        return post


@app.route('/models/<int:model_id>/order')
def order(model_id):
    model = get_models(model_id)
    return render_template('order.html', model=model)


app.run(port=5000, host="0.0.0.0", debug=True)