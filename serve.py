# ライブラリ
from flask import Flask

# ルーティング
from app.routes.index import *


app = Flask(
  __name__,
  static_folder='./app/static/',
  template_folder='./app/templates/'
)


app.register_blueprint(index)


if __name__ == '__main__':
  app.debug = True
  app.run(host='localhost', port=8080)
