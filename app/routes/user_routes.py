from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from app.models.user import User
from app import db

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/api/list', methods=['GET'])
def get_users_api():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])