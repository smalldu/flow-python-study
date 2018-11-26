
from flask import Flask,request,render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
monment = Moment(app)
app.config['SECRET_KEY'] = 'hard to guess string'

@app.route('/')
def index():
    # user_agent = request.headers.get('User-Agent')
    # print(app.url_map)
    return render_template('index.html',current_time = datetime.utcnow())

if __name__ == '__main__':
    manager.run()
