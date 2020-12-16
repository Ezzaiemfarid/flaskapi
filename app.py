from flask import Flask, request, jsonify
from tensorflow import keras
import numpy as np
model = keras.models.load_model('m.h5')
def predict(IS, pachymetrie, pattern, couleur, DBFS):
    yy = np.array([[IS, pachymetrie, pattern, couleur, DBFS]], np.float)

    prediction = model.predict(yy, batch_size=None, verbose=0, steps=None)
    print(prediction)
    return prediction
app = Flask(__name__)

@app.route('/')
def hello():
    
    return 'atef dahmen'
@app.route('/j',methods=['POST','GET'])
def hello_world():
    req_data = request.get_json()
    a = req_data['a']
    b = req_data['b']
    c = req_data['c']
    d = req_data['d']
    f = req_data['f']
    x = predict(float(a),float(b),float(c),float(d),float(f))[0][0]
    return jsonify(str(x))


if __name__ == '__main__':
    app.run()
