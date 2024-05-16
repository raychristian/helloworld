from flask import Flask
from config import config

app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def hello_world():
    secret_value = config.get_secret(config.SECRET_NAME)
    return f'Hello, World! Secret: {secret_value}'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
