from extensions import db

# ---------------- USERS ----------------
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    mobile_number = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(120))
    role = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), default="active")
    vendorId = db.Column(db.Integer)

    def to_dict(self):
        return vars(self)


#---------------- HUB ----------------
class Hubs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    hub_type = db.Column(db.String(50))
    vendor_id = db.Column(db.Integer)
    status = db.Column(db.String(20), default="active")

    def to_dict(self):
        return vars(self)


# ---------------- HUB PRODUCT ----------------
class HubProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hub_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)
    stock_quantity = db.Column(db.Integer)
    status = db.Column(db.String(20), default="active")

    def to_dict(self):
        return vars(self)


# ---------------- STOCK MOVEMENT ----------------
class StockMovement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer)
    from_hub_id = db.Column(db.Integer)
    to_hub_id = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    movement_type = db.Column(db.String(50))
    status = db.Column(db.String(20), default="initiated")

    def to_dict(self):
        return vars(self)


# ---------------- CART ----------------
class CartModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    status = db.Column(db.String(20), default="active")

    def to_dict(self):
        return vars(self)