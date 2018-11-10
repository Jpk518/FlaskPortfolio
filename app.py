from flask import Flask, render_template
import json

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

workplaces = [
    {
        'Title': 'General Dynamics',
        'About': 'Military',
        'Accomplishments': 'Networking'
    },
    {
        'Title': 'DuXion Motors',
        'About': 'Aerospace Startup',
        'Accomplishments': 'Thermal Systems'
    },
    {
        'Title': 'Rheinmetall Landsysteme',
        'About': 'Military',
        'Accomplishments': 'Networking'
    },
    {
        'Title': 'Bell Canada',
        'About': 'Radio/Telephone Company',
        'Accomplishments': 'Networking'
    }
]

projects = [
    {
        'Title': 'Kraken Robotics',
        'About': 'Robotics',
        'Accomplishments': 'Software'
    },
    {
        'Title': 'Paradigm Hyperloop',
        'About': 'Robotics',
        'Accomplishments': 'Software'
    },
    {
        'Title': 'Personal Projects',
        'About': 'Robotics',
        'Accomplishments': 'Software'
    },
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', workplaces=workplaces, projects=projects)

if __name__ == 'main':
    app.run(debug=True)