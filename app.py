    #1.Pandas for dataframe
import pandas as pd

    #2. NumPy to peform Calculations
import numpy as np

    #3. To split data
from sklearn.model_selection import train_test_split

    #4. For Linear Regression
from sklearn.linear_model import LinearRegression

    #For UI
import streamlit as st


# Pre-processing data

# Reading CSV file
cars_data=pd.read_csv("cars_sampled.csv" )
#Creating copy
cars=cars_data.copy()

# Summarizing data
pd.set_option('display.float_format', lambda x: '%.2f' % x)

# Data cleaning
# Dropping unwanted columns
col=['name','dateCrawled','dateCreated','postalCode','lastSeen']
cars=cars.drop(columns=col, axis=1)

# Removing duplicate records
cars.drop_duplicates(keep='first',inplace=True)
#470 duplicate records

# Variable yearOfRegistration
yearwise_count=cars['yearOfRegistration'].value_counts().sort_index()

sum(cars['yearOfRegistration'] > 2018)
sum(cars['yearOfRegistration'] < 1950)

# Working range- 1950 and 2018


sum(cars['price'] > 150000)
sum(cars['price'] < 100)
# Working range- 100 and 150000


sum(cars['powerPS'] > 500)
sum(cars['powerPS'] < 10)
# Working range- 10 and 500

# Working range of data

cars = cars[
        (cars.yearOfRegistration <= 2018)
      & (cars.yearOfRegistration >= 1950)
      & (cars.price >= 100)
      & (cars.price <= 150000)
      & (cars.powerPS >= 10)
      & (cars.powerPS <= 500)]
# ~6700 records are dropped

# Further to simplify- variable reduction
# Combine yearOfRegistration and monthOfRegistration into a single variable using .loc
cars.loc[:, 'Age'] = (2018 - cars.loc[:, 'yearOfRegistration']) + (cars.loc[:, 'monthOfRegistration'] / 12)

# Round Age to two decimal places
cars.loc[:, 'Age'] = round(cars.loc[:, 'Age'], 2)

# Dropping yearOfRegistration and monthOfRegistration
cars=cars.drop(columns=['yearOfRegistration','monthOfRegistration'], axis=1)

# MODEL BUILDING WITH OMITTED DATA
# Separating input and output features
# OMITTING MISSING VALUES
cars_omit=cars.dropna(axis=0)

# Converting categorical variables to dummy variables
cars_omit=pd.get_dummies(cars_omit,drop_first=True)
x1 = cars_omit.drop(['price'], axis='columns', inplace=False)
x1 = cars_omit[['powerPS', 'kilometer', 'Age']]
x1.columns = ['powerPS', 'kilometer', 'Age']  # Set column names
y1 = cars_omit['price']

# Train a model
model = LinearRegression()
model.fit(x1, y1)

#Taking User Input
st.header("Predicting Price of Pre-Owned Cars")
#user =st.text_input("Enter Complaint Narrative: ")

# Initialize an integer variable
int_val1, int_val2,int_val3 = 0,0,0

#Power
powerPS=st.text_input("Enter Power of Vehicle:")
try:
    int_val1= int(powerPS)
except ValueError:
    st.error('Please enter a valid integer.')

#Distance
kilometer=st.text_input("Enter Distance travelled in Kilometres by the Vehicle:")
try:
    int_val2 = int(kilometer)
except ValueError:
    st.error('Please enter a valid integer.')

#Age
Age=st.text_input('Enter Age of Vehicle in Years:')
try:
    int_val3 = int(Age)
except ValueError:
    st.error('Please enter a valid integer.')

b1=st.button("Submit") #button

data = np.array([int_val1, int_val2, int_val3])
data=data.reshape(1, -1)

# Make predictions
predictions = model.predict(data)

if b1:
    st.write("Price in INR:")
    val=np.round(predictions,2)
    st.write(val)
