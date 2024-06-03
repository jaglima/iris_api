import pandas as pd
import pickle


def irisModel(payload):
    uri = "model/mlruns/460877760308877689/67ed8f1d5bf045099a60a2e39dc50e7d/artifacts/random_forest_model"
    model_uri = f"{uri}/model.pkl"
    feat_uri = f"{uri}/feat_encoder.pkl"
    target_uri = f"{uri}/target_encoder.pkl"

    # Use the loaded Label Encoder to inverse transform
    cols = [
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width",
    ]
    input_data = pd.DataFrame(payload, columns=cols)
    print(input_data)

    # Load the Label Encoder
    with open(feat_uri, "rb") as f:
        loaded_feat = pickle.load(f)
    features = loaded_feat.transform(input_data)
    print(features)

    # Perform inference
    features = pd.DataFrame(features, columns=cols)
    with open(model_uri, "rb") as m:
        loaded_model = pickle.load(m)
    predictions = loaded_model.predict(features)
    print(predictions)
    
    # Load the Label Encoder
    with open(target_uri, "rb") as le:
        loaded_le = pickle.load(le)
    original_label = loaded_le.inverse_transform(predictions)
    print(original_label)

    return original_label.tolist()
