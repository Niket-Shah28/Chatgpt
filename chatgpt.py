from flask import Flask,render_template,jsonify,request
import requests
import openai
import os
openai.api_key=os.getenv('API_KEY')

app=Flask(__name__)

@app.route("/",methods=['GET'])
def home():
    return render_template("index.html")

@app.route("/",methods=['POST'])
def post():
    messages=request.form['information']
    messages_send=[{"role":"user","content":messages}]
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages_send)
    reply = chat.choices[0].message.content
    return f"{reply}"
    
    

if __name__ == '__main__':
    app.run()