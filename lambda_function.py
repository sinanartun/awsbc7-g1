import json
import boto3
import pandas as pd
import joblib
import os
import numpy as np
import lightgbm

# Constants
BUCKET_NAME = 'fiyattahmin'
LOCAL_MODEL_PATH = "/tmp/model-1.pkl"
REMOTE_MODEL_PATH = "model-1.pkl"

def lambda_handler(event, context):
    # CORS handlin

    # # Validating and extracting query parameters
    # query_params = event.get("queryStringParameters", {})
    

    
    # Load model
    if not os.path.exists(LOCAL_MODEL_PATH):
        boto3.client("s3").download_file(BUCKET_NAME, REMOTE_MODEL_PATH, LOCAL_MODEL_PATH)

    # Predict
    try:
        trained_model = joblib.load(LOCAL_MODEL_PATH)
        input_data = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]])
        fiyat_prediction = trained_model.predict(input_data)
        fiyat = int(np.round(fiyat_prediction[0]))
    # except NotFittedError:
    #     return {"statusCode": 500, "body": "Model not fitted"}
    except Exception as e:
        return {"statusCode": 500, "body": f"Prediction error: {str(e)}"}

    # Response
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
        },
        "body": json.dumps({"fiyat": fiyat})
    }

# sss = lambda_handler(1,2)
# print(sss)