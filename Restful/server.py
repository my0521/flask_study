from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world'

# http://127.0.0.1:5000/user/my
@app.route('/user/<username>')
def user(username):
    print(username)
    print(type(username))
    return 'hello ' + username

# http://127.0.0.1:5000/user/my/friends
@app.route('/user/<username>/friends')
def user_friends(username):
    print(username)
    print(type(username))
    return 'hello ' + username +  'They are your friends.'

# http://127.0.0.1:5000/page/1
@app.route('/page/<int:num>')
def page(num):
    print(num)
    print(type(num))
    return 'hello world'


if __name__ == '__main__':
    app.run(port=5000, debug=True)