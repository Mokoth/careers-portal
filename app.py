from flask import Flask, render_template, url_for, jsonify

app = Flask(__name__)

JOBS = [
  {'id': 1, 'title': 'Junior Flask developer', 'location': 'Nashvile', 'salary': 120000},
  {'id': 2, 'title': 'Senior Python developer', 'location': 'Greenfield', 'salary': 100000},
  {'id': 3, 'title': '.NET developer', 'location': 'Mombay', 'salary': 150000},
  {'id': 4, 'title': 'FastAPI developer', 'location': 'Remote'},
  {'id': 5, 'title': 'Fullstack developer', 'location': 'Brazil', 'salary': 220000}
]

@app.route('/')
def index():
  return render_template('home.html', jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)