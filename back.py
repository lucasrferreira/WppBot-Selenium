from flask import Flask, render_template, request, jsonify, redirect, url_for
from apscheduler.schedulers.background import BackgroundScheduler
import atexit

class Group:
   def __init__(self, group_name, is_on):
      self.group_name = group_name
      self.is_on = is_on
   

app = Flask(__name__)
cron = BackgroundScheduler(daemon=True)

@app.route('/')
def index():
    return redirect(url_for('get_groups'))

@app.route('/groups', methods=['GET'])
def get_groups():
   g1 = Group("Group1", True)
   g2 = Group("Group2", False)
   g3 = Group("Group3", True)
   g4 = Group("Group4", True)
   groups = [g1,g2,g3,g4]
   print(groups)
   return render_template('groups.html', groups = groups)

@app.route('/groups', methods=['POST'])
def post_groups():
   requent_form = request.form
   print(requent_form)
   return render_template('groups.html', groups = requent_form)

@app.route('/startbot/', methods=['GET'])
def startbot():
   from wppbot import WppApi
   wpp = WppApi(60)
   chats = wpp.get_chat_names()

   data = {'message': chats}
   print(data)

def fetch():
   print("fetched")

cron.add_job(fetch, 'interval', seconds=1)


cron.start()
atexit.register(lambda: cron.shutdown(wait=False))
if __name__ == '__main__':
   app.run(debug=True,host='0.0.0.0')