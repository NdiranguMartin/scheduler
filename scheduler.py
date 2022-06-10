from flask import Flask, render_template
app = Flask(__name__)

schedules = [
    {
        'name': 'Phil Karanja',
        'shift': 'Day',
        'week': 'June 6',
        'days': 'Tuesday, Wednesday, Thursday, Friday, Saturday'
    }
    ,{
        'name': 'Jane Doe',
        'shift': 'Night',
        'week': 'This week',
        'days': 'Monday, Tuesday, Wednesday, Thursday'
    }
]
@app.route("/")
def greetings():
    return render_template("home.html", schedule = schedules)

@app.route("/about")
def about():
    return render_template("about.html", title = 'About')


if __name__ == "__main__":
    app.run(debug=True)