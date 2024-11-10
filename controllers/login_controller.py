from flask import render_template, request, redirect, url_for, flash, session
from models import User
from datetime import timedelta
from usecases.login_usecase import LoginUseCase

from flask import render_template, request, redirect, url_for, flash, session, jsonify
from models import User
from datetime import timedelta
from usecases.login_usecase import LoginUseCase
import cv2
import base64
import numpy as np

class LoginController:
    def login(self, request):
        landmarks = []  # Inicializa a lista de landmarks

        if request.method == 'POST':
            email = request.form.get('email')
            photo_data = request.form.get('photo')

            # Buscar o usuário pelo email
            user = User.query.filter_by(email=email).first()
            if user:
                # Verificar a face usando o use case de login
                login_use_case = LoginUseCase()
                success, landmarks = login_use_case.face_recognition(user.photo_path, photo_data)
                print(f'Landmarks recebidos do use case: {landmarks}')  # Debug

                if success:
                    session.permanent = True
                    session['user_id'] = user.id
                    session['email'] = user.email
                    session['photo_path'] = user.photo_path
                    session.modified = True

                    flash('Login realizado com sucesso!', 'success')
                    return redirect(url_for('bp.dashboard'))
                else:
                    flash('Falha na verificação facial. Tente novamente.', 'danger')
            else:
                flash('Usuário não encontrado.', 'danger')

        return render_template('login.html', landmarks=landmarks)  # Passa os landmarks para o template