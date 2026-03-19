from flask import Blueprint, jsonify,request
from models import Users
from extensions import db

users_bp = Blueprint('users_bp', __name__)

@users_bp.route('/')
def home():
    return 'Hai Vijayakumar your API running successfully'

@users_bp.route('/users', methods=['GET'])
def get_users():
    users = Users.query.all()

    user_list = []
    for user in users:
        user_list.append({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "mobile_number": user.mobile_number,
            "role": user.role,
            "status": user.status,
            "vendorId": user.vendorId
        })

    return jsonify({
        "count": len(user_list),
        "users": user_list
    })

@users_bp.route('/users_1', methods=['POST'])
def add_user():
    data = request.json 

    # validate required fields
    entry_field = ['name', 'email', 'mobile_number', 'role']
    for field in entry_field:
        if not data.get(field):
            return jsonify({"error": f"{field} is required"})

    new_user = Users(
        name=data.get('name'),
        email=data.get('email'),
        mobile_number=data.get('mobile_number'),
        password=data.get('password'),
        role=data.get('role'),
        status=data.get('status', 'active'), 
        vendorId=data.get('vendorId')
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "message": "User added successfully",
        "user": {
            "id": new_user.id,
            "name": new_user.name,
            "email": new_user.email,
            "mobile_number": new_user.mobile_number,
            "role": new_user.role,
            "status": new_user.status,
            "vendorId": new_user.vendorId
        }
    })
@users_bp.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        users = Users.query.all()
        return jsonify([u.to_dict() for u in users])

    elif request.method == 'POST':
        data = request.json

        new_user = Users(
            name=data.get('name'),


            email=data.get('email')
        )
        users_bp.session.add(new_user)
        users_bp.session.commit()

        return jsonify({"Message": "User added"})