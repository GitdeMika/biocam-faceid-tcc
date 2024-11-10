# /controllers/user_controller.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from usecases.register_usecase import RegisterUser

bp = Blueprint('bp', __name__)


class UsersController:
    def register(self):
        if request.method == 'POST':
            name = request.form.get('name')
            email = request.form.get('email')
            password = request.form.get('password')
            photo_data = request.form.get('photo')

            # Cria uma instância do use case
            register_user = RegisterUser(name, email, password, photo_data)
            success, message = register_user.execute()

            flash(message, 'success' if success else 'danger')
            if success:
                return redirect(url_for('bp.login'))

        return render_template('register.html')


@bp.route('/register', methods=['GET', 'POST'])
def register_route():
    controller = UsersController()
    return controller.register()
