import os
from flask_migrate import MigrateCommand, Migrate
from APP.user.models import User
from flask_script import Manager
from APP import create_app
from APP.extension import db

# 导入所有app配置
app = create_app(os.environ.get("FLASK_CONFIG") or 'default')
# 命令行
manager = Manager(app)
# 数据库迁移
migrate = Migrate(app, db)
manager.add_command("db", MigrateCommand)

# python manage.py db init
# python manage.py db migrate
# python manage.py db upgrade

if __name__ == '__main__':
    manager.run()