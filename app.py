from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the trained model
with open('House_Price_Prediction.pkl', 'rb') as file:
    model = pickle.load(file)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get input values from the form
        bedrooms = int(request.form['bedrooms'])
        bathrooms = float(request.form['bathrooms'])
        sqft_living = int(request.form['sqft_living'])
        sqft_lot = int(request.form['sqft_lot'])
        floors = float(request.form['floors'])
        waterfront = int(request.form['waterfront'])
        view = int(request.form['view'])
        condition = int(request.form['condition'])

        # Prepare input data for prediction
        input_data = [[bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, condition]]

        # Make the price prediction
        predicted_price = model.predict(input_data)[0]

        # Render the result template with predicted price
        return render_template('index.html', predicted_price=predicted_price)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=False)
