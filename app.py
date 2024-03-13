import streamlit as st
import pickle
import numpy as np

# Load the model from the file
with open('model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

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


data = np.array([int_val1, int_val2, int_val3])
data=data.reshape(1, -1)

# Make predictions
predictions = loaded_model.predict(data)
st.write("Price in INR:")
val=np.round(predictions,2)
st.write(-val)