#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

#import flask
from flask import Flask, render_template, request

from helper import prediction_f
from helper import message_f

#create a flask object
app = Flask(__name__)

#create route 
#use decorators to create routes 

# for each route you define one python function to be executed (and this will be the result)
@app.route('/', methods = ['POST','GET'])
def index():
    # the python logic that will be run when the route is called
    if request.method == 'POST':
        # do stuff
        d = {'Female': 0, 'Male':1, 'Service': 1, 'Product': 0, 'Yes': 1, 'No':0, 'Intern':0, 'Junior':1, 
             'Mid Level':2, 'Senior':3, 'Senior Executive':4, 'C-Suite':5}
        p1 = request.form['parameter 1']
        p3 = request.form['parameter 3']
        p4 = request.form['parameter 4']
        p5 = request.form['parameter 5']
        p6 = request.form['parameter 6']
        
        gender = d[p1]
        c_type = 0
        wfh = d[p3]
        seniority = d[p4]
        resource = int(p5)
        mfatigue = float(p6)
        par = [[gender, c_type, wfh, seniority, resource, mfatigue]]
        
        rate = prediction_f(par)
        
        
        prediction = message_f(rate)
        
        return render_template('main.html', prediction = prediction, rate = rate)
    else:
        return render_template('main.html')
    
#running our flask app
if __name__ == "__main__" : 
    app.run(debug = True)