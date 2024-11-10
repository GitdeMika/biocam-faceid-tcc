from flask import Blueprint, flash, jsonify, render_template, request, session, redirect, url_for, send_from_directory
from controllers.users_controller import UsersController
from controllers.login_controller import LoginController
import os

users_controller = UsersController()
login_controller = LoginController()

bp = Blueprint('bp', __name__)


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    return users_controller.register()


@bp.route('/login', methods=['GET', 'POST'])
def login():
    return login_controller.login(request=request)


@bp.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        email = session['email']
        photo_path = session['photo_path']
        filename = os.path.basename(photo_path)
        return render_template('dashboard.html', email=email, filename=filename)
    else:
        return redirect(url_for('bp.login'))



@bp.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('email', None)
    flash('Você foi deslogado com sucesso!', 'info')
    return redirect(url_for('bp.login'))


@bp.before_request
def make_session_permanent():
    session.permanent = True


@bp.route('/<filename>')
def uploads(filename):
    return send_from_directory('uploads', filename)
