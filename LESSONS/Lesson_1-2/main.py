from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello, World!!!!!'


@app.route('/user_name/<user>')
def hello_user(user):
    print(user, type(user))
    return f'Hello, {user}!'


@app.route('/<int:number>')
def number(number):
    print(number, type(number))
    return f'{number}!'


@app.route('/files/<filepath>')
def show_file(filepath):
    print(filepath, type(filepath))
    return f'File located at: {filepath}'


@app.route('/user/<uuid:user_id>')  # 32 символа в 16-чной кодировке fmt: 8-4-4-4-12
def show_user_profile_by_uuid(user_id):
    print(user_id, type(user_id))
    return f'User with UUID: {user_id}'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
