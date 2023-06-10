from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names', methods = ['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/get_house_types_names', methods = ['GET'])
def get_house_type_names():
    response = jsonify({
        'house_types': util.get_house_type_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_home_price', methods = ['GET','POST'])
def predict_home_price():
    bathrooms = request.form.get('bathrooms')
    sqft = request.form.get('total_sqft')
    location = request.form.get('location')
    bedrooms = request.form.get('bedrooms')
    receptions = request.form.get('receptions')
    house_type = request.form.get('house_type')
    print(location)
    print(bedrooms)
    print(bathrooms)
    response = jsonify({
        'estimated_price': util.get_estimated_price(location, sqft, bedrooms, bathrooms, receptions, house_type)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    with app.app_context():
        print("Starting Python Flask Server For Home Price Prediction..")
        util.load_saved_artifacts()
        print(util.__data_columns)
        print(util.__house_types)
        app.run()
