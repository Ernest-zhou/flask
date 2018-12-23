from flask import Flask,render_template,Blueprint
import threading
import multiprocessing
import time

def start_web():
    app = Flask(__name__)
    @app.route('/')
    def hello():
        reutrn "Hello everyonr1"
    @app.route('/user')
    def user():
        return "user.html"
    app.run(debug=True)

Count = 0
lock = threading.Lock()
l = []
def Function():
    global Count
    lock.acquire()
    Count += 1
    return Count
    lock.release()
a = threading.Thread(target = start_web, name = "Thread_one")
for i in range(10):
   threading.Thread(target = Function, name = "Thread_two").start()
   l.append(Count)
raw_input("Enter any key to continue.")

