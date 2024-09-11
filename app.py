import atexit
import requests
from flask import Flask, render_template
from apscheduler.schedulers.background import BackgroundScheduler

def find_unsubscribe_messages(messages):


def get_message():
    response = requests.get("http://hackathons.masterschool.com:3030/team/getMessages/sgs")
    data = response.json()
    find_unsubscribe_messages(data)
    print(data)
def init():
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=get_message, trigger="interval", seconds=60)
    scheduler.start()

    # Shut down the scheduler when exiting the app
    atexit.register(lambda: scheduler.shutdown())

init()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


