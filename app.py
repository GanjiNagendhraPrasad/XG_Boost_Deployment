from flask import Flask, render_template, request
import numpy as np
import pickle

# Load trained AdaBoost model
with open('xgb.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None

    if request.method == 'POST':
        features = np.array([[

            # ===== Mean Features =====
            float(request.form['radius_mean']),
            float(request.form['texture_mean']),
            float(request.form['perimeter_mean']),
            float(request.form['area_mean']),
            float(request.form['smoothness_mean']),
            float(request.form['compactness_mean']),
            float(request.form['concavity_mean']),
            float(request.form['concave_points_mean']),
            float(request.form['symmetry_mean']),
            float(request.form['fractal_dimension_mean']),

            # ===== Standard Error Features =====
            float(request.form['radius_se']),
            float(request.form['texture_se']),
            float(request.form['perimeter_se']),
            float(request.form['area_se']),
            float(request.form['smoothness_se']),
            float(request.form['compactness_se']),
            float(request.form['concavity_se']),
            float(request.form['concave_points_se']),
            float(request.form['symmetry_se']),
            float(request.form['fractal_dimension_se']),

            # ===== Worst Features =====
            float(request.form['radius_worst']),
            float(request.form['texture_worst']),
            float(request.form['perimeter_worst']),
            float(request.form['area_worst']),
            float(request.form['smoothness_worst']),
            float(request.form['compactness_worst']),
            float(request.form['concavity_worst']),
            float(request.form['concave_points_worst']),
            float(request.form['symmetry_worst']),
            float(request.form['fractal_dimension_worst'])

        ]])

        pred = model.predict(features)[0]

        if pred == 1:
            prediction = "Malignant (Cancerous)"
        else:
            prediction = "Benign (Non-Cancerous)"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)