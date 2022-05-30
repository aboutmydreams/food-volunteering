from flask import Flask,request,jsonify,url_for,render_template
import json,write_data
def check_root():
    payload = {"number":request.json['username'],"passwd":request.json['password']}
    data = str(payload['number'])+':::'+str(payload['passwd'])
    with open('data/root.txt','r') as f0:
        f00 = f0.read()
    if len(data) > 3 and data in f00:
        return '<h3>Bad username or password.</h3>'#render_template("set.html")
    else:
        return jsonify({'status':'error'})

def qianduan_get():
    
