from flask import Flask, render_template, url_for, flash, redirect

from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '2d8d66f3a6aadec8249df2c42b192685'

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


@app.route('/register', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        # flash = message provided by flask for ui  2nd parameter is bootstrap class for it
        flash(f'Account Created for  {form.username.data}', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Registration', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
