from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Club History',
        'about': 'Discover the rich legacy of Real Madrid, from its founding to its rise as a football powerhouse.'
    },
    {
        'id': 2,
        'title': 'Legendary Players',
        'about': 'Learn about the greatest players who have ever worn the white jersey.'
    },
    {
        'id': 3,
        'title': 'Recent Achievements',
        'about': 'Stay updated with Real Madrid\'s latest triumphs and records.'
    }
]



@app.route("/")
def hello():
    return render_template("home.html", jobs=JOBS)


@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
