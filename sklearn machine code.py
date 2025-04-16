# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 17:51:08 2025

@author: test
"""

import pandas as pd

from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.metrics import accuracy_score

# Step 1: Create the dataset (you can also Load this from CSV)
data = {
'Day': ['Sunny', ' Windy', 'Sunny', 'Windy', 'Windy', 'Sunny', 'Windy', 'Sunny', 'Sunny'],
'Temprature': ['Cool', 'Cool', 'Hot', 'Hot', 'Hot', 'Cool', 'Hot', 'Hot', 'Hot'],
'Class': ['Play', 'Not Play', 'Not Play', 'Play', 'Play', 'Play', 'Not Play', 'Play', 'Play']
}

df = pd.DataFrame(data)

# Step 2: Split features and target

X_raw = df[['Day', 'Temprature' ]] # Features
Y_raw = df['Class'] # Target

# Step 3: Encode categorical features

onehot_encoder = OneHotEncoder( )

X_encoded = onehot_encoder.fit_transform(X_raw).toarray()
# Step 4: Encode target labels

label_encoder = LabelEncoder()

Y_encoded = label_encoder.fit_transform(Y_raw)

# Step 5: Split into train and test

X_train, X_test, Y_train, Y_test = train_test_split(X_encoded, Y_encoded, test_size=0.3, random_state=42)
# Step 6: Train the Naive Bayes classifier

model = GaussianNB()

model.fit(X_train, Y_train)

# Step 7: Predict on test set and print accuracy

y_pred = model.predict(X_test)

print("Test Accuracy:", accuracy_score(Y_test, y_pred))

# Step 8: Predict a single new instance (e.g., Windy & Cool)

# Fix; Pass new instance aS DataFrame with column names matching the training data
new_instance = pd.DataFrame([['Windy', 'Cool']], columns=['Day','Temprature'])
new_instance_encoded = onehot_encoder.transform(new_instance).toarray( )

predicted_class = model.predict(new_instance_encoded)
predicted_label = label_encoder.inverse_transform(predicted_class)[0]
print("Prediction for Day-Windy, Temp=Cool:", predicted_label)