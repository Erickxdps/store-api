from app.database import db

class Producto(db.Model):
    __tablename__ = "productos"
    # Define las columnas de la tabla `users`
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float(), nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    # Inicializa la clase `Producto`
    def __init__(self, name, description, price, stock):
        self.name=name
        self.description=description
        self.price=float(price)
        self.stock=int(stock)

    # Guarda un usuario en la base de datos
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Obtiene todos los animales de la base de datos
    @staticmethod
    def get_all():
        return Producto.query.all()

    # Obtiene un animal por su ID
    @staticmethod
    def get_by_id(id):
        return Producto.query.get(id)

    # Actualiza un animal en la base de datos
    def update(self, name=None, description=None, price=None, stock=None):
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if price is not None:
            self.price = price
        if stock is not None:
            self.stock = stock
        db.session.commit()

    # Elimina un animal de la base de datos
    def delete(self):
        db.session.delete(self)
        db.session.commit()
