#!/bin/env python3
from time import sleep
from flask import Flask, render_template
import atexit
import motor

motor.setup()
app = Flask(__name__)

@app.route('/')
def hello():
	return '<a href="/home">here</a>'

@app.route('/home/')
def home():
    return render_template('index.html')
	
@app.route('/set/<value>')
def set(value):
    value = int(value)
    try:
        if value > 0:
            for i in range(value):
                motor.fw(0.008)
        elif value < 0:
            for i in range(-value):
                motor.bw(0.008)
        return "Done moving - position: %d" % (value)
    except:
        return "Error"


atexit.register(motor.cleanup)
