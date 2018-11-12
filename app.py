from flask import Flask, render_template
import json

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True


with open("json/workplaces.json","r") as workFile:
    workplaces = json.load(workFile)
with open("json/projects.json", "r") as projectFile:
    projects = json.load(projectFile)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', workplaces=workplaces, projects=projects)

@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == 'main':
    app.run(debug=True)