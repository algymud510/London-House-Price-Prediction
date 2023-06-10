import json
import pickle
import sklearn
import numpy as np


__locations = None
__data_columns = None
__model = None
__house_types = None
x = None


def get_estimated_price(location,sqft,bedrooms,baths,receptions,house_type):
    global __data_columns
    global x
    try:
        loc_index = __data_columns.index(location.lower())
        loc_index2 = __data_columns.index(house_type.lower())
    except:
        loc_index = -1
        loc_index2 = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bedrooms
    x[2] = baths
    x[3] = receptions
    if loc_index>=0:
        x[loc_index] = 1
    if loc_index2>=0:
        x[loc_index2] = 1
    print(x)
    print(len(x))
    return round(__model.predict([x])[0], 2)


def load_saved_artifacts():
    print("loading saved artifacts__start")
    global __data_columns
    global __locations
    global __model
    global __house_types

    with open("C:/Users/meeta/School/House price prediction/London ends/server/artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[12:]
        __house_types = __data_columns[5:11]

    if __model is None:
        with open("C:/Users/meeta/School/House price prediction/London ends/server/artifacts/london_home_prices_model.pickle", 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")


def get_location_names():
    global __locations
    return __locations

def get_house_type_names():
    global __house_types
    return __house_types

def get_data_columns():
    global __data_columns
    return __data_columns


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price("Tower Hamlets London Boro",1100, 2, 3, 2, 'Duplex'))