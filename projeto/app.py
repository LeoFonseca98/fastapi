from flask import Flask, jsonify
import os
from dotenv import load_dotenv
from pyngrok import ngrok
import random


load_dotenv()

ngrok_token = os.getenv("AUTHTOKEN_NGROK")
ngrok.set_auth_token(ngrok_token)


app = Flask(__name__)

d = {
    "numero": 2,
    "nome": "Leonardo Moreira Fonseca",
    "idade": 26,
    "cidade": "Desterro",
    "pais": "Brasil"
}

@app.route("/")
def hello_world():
    return "<h3>TO CHECK IN PUT ADD '/input' TO THE URL AND TO CHECK OUT PUT ADD '/output' TO THE URL.</h3>"

@app.route("/input")
def input_data():
    return jsonify(d)

@app.route("/output", methods=['GET', 'POST'])
def pred_json():
    pred = random.choice(["positive", "negative"])
    nd = d.copy() 
    nd["predication"] = pred
    return jsonify(nd)

if __name__ == "__main__":

    public_url = ngrok.connect(5000)
    print(f"Public URL: {public_url}")
    

    app.run(port=5000)
