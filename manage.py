# Thirdparty libraries imports
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

# Local applications imports
# app config
from instance.config import AppConfig
from app import create_app

# models
from app.api.models.user import User
from app.api.models.databases import db

app = create_app(AppConfig)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
