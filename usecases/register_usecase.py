import base64
import bcrypt
from datetime import datetime, timezone
from models import db, User


class RegisterUser:
    def __init__(self, name, email, password, photo_data):
        self.name = name
        self.email = email
        self.password = password
        self.photo_data = photo_data

    def execute(self):
        # Verifica se a foto foi capturada
        if self.photo_data:
            header, encoded = self.photo_data.split(',', 1)
            data = base64.b64decode(encoded)

            # Obtem o timestamp atual
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            photo_path = f'uploads/{self.name}_{timestamp}.jpg'

            # Salva a foto em um arquivo
            with open(photo_path, 'wb') as f:
                f.write(data)

            # Criptografa a senha com bcrypt
            pwd_hash = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt())

            # Cria um novo usuário
            new_user = User(name=self.name, email=self.email, password_hash=pwd_hash, photo_path=photo_path)

            # Adiciona o usuario no banco Mysql
            db.session.add(new_user)
            db.session.commit()

            return True, 'Usuário cadastrado com sucesso'
        return False, 'Erro ao cadastrar o usuário'


