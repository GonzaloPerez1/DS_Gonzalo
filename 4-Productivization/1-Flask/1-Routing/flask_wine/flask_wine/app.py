from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json


app = Flask(__name__)



@app.route('/health/', methods=['GET'])
def health():
    return 'everything ok here'

@app.route('/api/', methods=['POST'])
def makecalc():
    data = request.get_json()
    prediction = np.array2string(model.predict(data))
    return jsonify(prediction)


modelfile = './models/final_prediction.pickle'
model = p.load(open(modelfile, 'rb'))

print(type(model))
#print('hello')

if __name__ == '__main__':
    # modelfile = './models/final_prediction.pickle'
    # model = p.load(open(modelfile, 'rb')

    print('hello')
    app.run(debug=False)
