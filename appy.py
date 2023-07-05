from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'Title': 'Data Analyst',
        'location': 'Bangaluru India',
        'Salary': 'Rs. 10,000,00'
    },
    {
        'id': 2,
        'Title': 'Software Engineer',
        'location': 'Hyderabad India',
        'Salary': 'Rs. 9,000,00'
    },
    {
        'id': 3,
        'Title': 'Devops Engineer',
        'location': 'Hyderabad India',
        'Salary': 'Rs. 15,000,00'
    },
    {
        'id': 4,
        'Title': 'Devops Engineer',
        'location': 'Singapore India',
        'Salary': 'Rm. 15,000'
    }
]


@app.route("/")
def hello_vijesh():
    return render_template('Home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
