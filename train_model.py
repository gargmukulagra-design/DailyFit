import pandas as pd
import sklearn

df = pd.read_csv(
    "dailyfit_realistic_synthetic_dataset_5000_rows.csv"
)

print(df.head())
print(df.shape)

#changing sex column from object datatype to Number
df["sex"]=df["sex"].map({"Male" : 0 , "Female" : 1})

print(df.head())

x = df[["age","sex","height_cm","weight_kg","bmi","avg_surplus","days"]]
y = df["weight_change"]

print(x.head())
print(y.head())

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)

from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(
    X_train,
    y_train
)
print("Model trained successfully!")

predictions = model.predict(X_test)
print(predictions[:10])

from sklearn.metrics import mean_absolute_error

mae = mean_absolute_error(
    y_test,
    predictions
)

print("MAE =", mae)

from sklearn.metrics import r2_score

r2 = r2_score(
    y_test,
    predictions
)

print("R2 =", r2)

import pickle

with open(
    "weight_model.pkl",
    "wb"
) as f:

    pickle.dump(
        model,
        f
    )