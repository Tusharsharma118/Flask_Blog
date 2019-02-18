from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Helix',
        'title': 'First Post',
        'content': 'This is my first Post!',
        'dated': 'February 12, 2019'
    },
    {
        'author': 'Helix Sama',
        'title': 'Second Post',
        'content': 'This is my second Post!',
        'dated': 'February '
    }
]


@app.route('/')
@app.route('/home')
def home():
    title = 'Home!'
    return render_template('home.html', title=title, posts= posts)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
