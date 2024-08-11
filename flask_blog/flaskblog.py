from flask import Flask, render_template, url_for

app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(debug=True)
