import streamlit as st
import pickle
import numpy as np 

st.set_page_config(layout="wide")

css_code = """
<style>
html, body, [class*="View"] {
    margin: 0px !important;
    padding: 0px !important;
}
.stApp {
    background-image: url("https://github.com/tejapeddi1/UMBC-DATA606-Capstone/blob/main/app/bg.png?raw=True");
    background-size: cover;
    background-position: right;
    background-repeat: no-repeat;
}
</style>
"""
st.markdown(css_code, unsafe_allow_html=True)

model = pickle.load(open('app/model.pkl', 'rb'))
scaler = pickle.load(open('app/scaler.pkl', 'rb'))

st.markdown("<div style='text-align: center;'><h1>Credit Card Default Prediction</h1></div>", unsafe_allow_html=True)

# Define feature names as per the dataset
feature_names = [
    'LIMIT_BAL', 'SEX', 'EDUCATION', 'MARRIAGE', 'AGE', 'PAY_1',
    'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6', 'BILL_AMT1', 'BILL_AMT2',
    'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6', 'PAY_AMT1',
    'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6'
]

# Create inputs for the features
feature_values = []

# Use columns to organize the inputs
input_rows = [
    feature_names[:5],
    feature_names[5:11],
    feature_names[11:17],
    feature_names[17:23],
]

# Mapping for dropdown options
sex_options = {1: 'male', 2: 'female'}
education_options = {1: 'graduate school', 2: 'university', 3: 'high school', 4: 'others'}
marriage_options = {1: 'married', 2: 'single', 3: 'divorce'}
pay_options = {-2: 'No transactions', -1: 'Paid in full', 0: 'Minimum due paid', 
               1: '1 month delay', 2: '2 months delay', 3: '3 months delay', 
               4: '4 months delay', 5: '5 months delay', 6: '6 months delay', 
               7: '7 months delay', 8: '8 months delay'}

bill_amts = []

for row in input_rows:
    cols = st.columns(len(row))
    for col, name in zip(cols, row):
        with col:
            if name == 'SEX':
                value = st.selectbox(name, options=[''] + list(sex_options.values()), index=0)
                value = [key for key, val in sex_options.items() if val == value][0] if value else 0
            elif name == 'EDUCATION':
                value = st.selectbox(name, options=[''] + list(education_options.values()), index=0)
                value = [key for key, val in education_options.items() if val == value][0] if value else 0
            elif name == 'MARRIAGE':
                value = st.selectbox(name, options=[''] + list(marriage_options.values()), index=0)
                value = [key for key, val in marriage_options.items() if val == value][0] if value else 0
            elif name.startswith('PAY_AMT'):
                value = st.number_input(name, value=0.0, format="%f", step=1.0)
            elif name.startswith('PAY_'):
                value = st.selectbox(name, options=[''] + list(pay_options.values()), index=0)
                value = [key for key, val in pay_options.items() if val == value][0] if value else 0
            elif name.startswith('BILL_AMT'):
                value = st.number_input(name, value=0.0, format="%f", step=1.0)
                bill_amts.append(value)
            else:
                value = st.number_input(name, value=0.0, format="%f", step=1.0)
            feature_values.append(value)

# Calculate CHANGE_AMT1 to CHANGE_AMT5
change_amts = [bill_amts[i+1] - bill_amts[i] for i in range(5)]

# Replace BILL_AMT1 to BILL_AMT6 with CHANGE_AMT1 to CHANGE_AMT5
feature_values = feature_values[:12] + change_amts + feature_values[18:]

data = np.array(feature_values).reshape(1, -1)

st.header('   ')
st.header('   ')

if st.button('Predict Default', key='predict_button', help="Click to predict whether there will be a default."):
    # Scale the input data using the loaded scaler
    data_scaled = scaler.transform(data)

    # Predict using the loaded model
    prediction = model.predict(data_scaled)

    # Display the prediction
    result = 'Default' if prediction[0] == 1 else 'Not Default'
    st.write(f'Prediction: **{result}**')

st.markdown("</div>", unsafe_allow_html=True)


# import streamlit as st
# import pickle
# import numpy as np 

# st.set_page_config(layout="wide")

# css_code = """
# <style>
# html, body, [class*="View"] {
#     margin: 0px !important;
#     padding: 0px !important;
# }
# .stApp {
#     background-image: url("https://github.com/tejapeddi1/UMBC-DATA606-Capstone/blob/main/app/bg.png?raw=True");
#     background-size: cover;
#     background-position: right;
#     background-repeat: no-repeat;
# }
# </style>
# """
# st.markdown(css_code, unsafe_allow_html=True)

# model = pickle.load(open('app/model.pkl', 'rb'))
# scaler = pickle.load(open('app/scaler.pkl', 'rb'))


# st.markdown("<div style='text-align: center;'><h1>Credit Card Default Prediction</h1></div>", unsafe_allow_html=True)

# # Define feature names as per the dataset
# feature_names = [
#     'LIMIT_BAL', 'SEX', 'EDUCATION', 'MARRIAGE', 'AGE', 'PAY_1',
#     'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6', 'BILL_AMT1', 'BILL_AMT2',
#     'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6', 'PAY_AMT1',
#     'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6'
# ]

# # Create inputs for the features
# feature_values = []

# # Use columns to organize the inputs
# input_rows = [
#     feature_names[:5],
#     feature_names[5:11],
#     feature_names[11:17],
#     feature_names[17:23],
# ]

# # Mapping for dropdown options
# sex_options = {1: 'male', 2: 'female'}
# education_options = {1: 'graduate school', 2: 'university', 3: 'high school', 4: 'others'}
# marriage_options = {1: 'married', 2: 'single', 3: 'divorce'}
# pay_options = {-2: 'No transactions', -1: 'Paid in full', 0: 'Minimum due paid', 
#                1: '1 month delay', 2: '2 months delay', 3: '3 months delay', 
#                4: '4 months delay', 5: '5 months delay', 6: '6 months delay', 
#                7: '7 months delay', 8: '8 months delay'}

# bill_amts = []

# for row in input_rows:
#     cols = st.columns(len(row))
#     for col, name in zip(cols, row):
#         with col:
#             if name == 'SEX':
#                 value = st.selectbox(name, options=list(sex_options.values()), index=0)
#                 value = [key for key, val in sex_options.items() if val == value][0]
#             elif name == 'EDUCATION':
#                 value = st.selectbox(name, options=list(education_options.values()), index=0)
#                 value = [key for key, val in education_options.items() if val == value][0]
#             elif name == 'MARRIAGE':
#                 value = st.selectbox(name, options=list(marriage_options.values()), index=0)
#                 value = [key for key, val in marriage_options.items() if val == value][0]
#             elif name.startswith('PAY_AMT'):
#                 value = st.number_input(name, value=0.0, format="%f", step=1.0)
#             elif name.startswith('PAY_'):
#                 value = st.selectbox(name, options=list(pay_options.values()), index=0)
#                 value = [key for key, val in pay_options.items() if val == value][0]
#             elif name.startswith('BILL_AMT'):
#                 value = st.number_input(name, value=0.0, format="%f", step=1.0)
#                 bill_amts.append(value)
#             else:
#                 value = st.number_input(name, value=0.0, format="%f", step=1.0)
#             feature_values.append(value)

# # Calculate CHANGE_AMT1 to CHANGE_AMT5
# change_amts = [bill_amts[i+1] - bill_amts[i] for i in range(5)]

# # Replace BILL_AMT1 to BILL_AMT6 with CHANGE_AMT1 to CHANGE_AMT5
# feature_values = feature_values[:12] + change_amts + feature_values[18:]

# data = np.array(feature_values).reshape(1, -1)

# st.header('   ')
# st.header('   ')


# if st.button('Predict Default', key='predict_button', help="Click to predict whether there will be a default."):
#     # Scale the input data using the loaded scaler
#     data_scaled = scaler.transform(data)

#     # Predict using the loaded model
#     prediction = model.predict(data_scaled)

#     # Display the prediction
#     result = 'Default' if prediction[0] == 1 else 'Not Default'
#     st.write(f'Prediction: **{result}**')


# st.markdown("</div>", unsafe_allow_html=True)
