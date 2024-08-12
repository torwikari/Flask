from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "0b8749e94baa815f9a13854edcfe84f5"

posts = [
    {
        "author": "Torwikari",
        "title": "Blog Post 1",
        "content": "1st post content",
        "date_posted": "11th August 2024",
    },
    {
        "author": "Torwikari",
        "title": "Blog Post 2",
        "content": "2nd post content",
        "date_posted": "12th August 2024",
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def aboutd():
    return render_template("about.html", title="About")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)
