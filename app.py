from flask import Flask, render_template, request
import joblib
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)

# Load both the model and CountVectorizer
model, featurizer = joblib.load('model_and_featurizer.pkl')

@app.route('/')
def home():
    return render_template('index.html')
 
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        url = request.form['url']
        data = [url]
        
        # Transform the data using the fitted CountVectorizer
        data_count = featurizer.transform(data)
        
        prediction = model.predict(data_count)[0]

        return render_template('result.html', prediction=prediction)



if __name__ == '__main__':
    app.run(debug=True)
