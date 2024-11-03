from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, LargeBinary, insert
from sqlalchemy.orm import Session

engine = create_engine('sqlite+pysqlite:///database.db', echo=True)
metadata = MetaData()


order_table = Table(
    'orders',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('price', Integer),
    Column('description', String(255)),
    Column('type', String(50)),
    Column('picture', LargeBinary, nullable=True),
)




def add_test_data():
    # Тестові дані для додавання
    test_data = [
        {
            "name": "Shoe Model A",
            "price": 100,
            "description": "Comfortable running shoes",
            "type": "Кросівки",
            "picture": None  # Тут можна додати байтові дані зображення
        },
        {
            "name": "Shoe Model B",
            "price": 150,
            "description": "Stylish sneakers",
            "type": "Шльопанці",
            "picture": None
        },
        {
            "name": "Shoe Model C",
            "price": 200,
            "description": "High-quality hiking boots",
            "type": "Лофери",
            "picture": None
        }
    ]


    with Session(engine) as session:
        for data in test_data:
            stmt = insert(order_table).values(data)
            session.execute(stmt)


        session.commit()



add_test_data()

metadata.create_all(engine)