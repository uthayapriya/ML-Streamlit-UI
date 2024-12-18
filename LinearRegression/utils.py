import pickle
import pandas as pd

standard_scaler_file = open("LinearRegressionModels/scaler.pkl", 'rb')
standard_scaler = pickle.load(standard_scaler_file)

ridge_model_file = open("LinearRegressionModels/ridge_model.pkl", 'rb')
ridge = pickle.load(ridge_model_file)



def predict_sales(parameters):
    column_headers = ["TV", "Radio", "Newspaper"]
    X_input_df = pd.DataFrame([parameters], columns=column_headers)
    X_test = standard_scaler.transform(X_input_df)
    y_pred = ridge.predict(X_test)

    standard_scaler_file.close()
    ridge_model_file.close()

    return y_pred[0]

def validate_input(input_lst):
    try:
        parameters = [int(x)/1000 for x in input_lst]
        return False if not all(x >= 0 for x in parameters) else parameters
    except Exception as e:
        return False