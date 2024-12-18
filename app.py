from flask import Flask
from config import Config
from models import db
from routes import bp
from datetime import timedelta

app = Flask(__name__)
app.config.from_object(Config)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB limit
app.config['MAX_CONTENT_LENGTH'] = Config.MAX_CONTENT_LENGTH  # Using from config

db.init_app(app)
app.permanent_session_lifetime = timedelta(minutes=15)
app.register_blueprint(bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)