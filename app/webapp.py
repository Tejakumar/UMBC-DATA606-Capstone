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

st.markdown("<div style='text-align: center;'><h1>Credit Card Default Prediction</h1></div>", unsafe_allow_html=True)

model = pickle.load(open('app/model.pkl', 'rb'))
scaler = pickle.load(open('app/scaler.pkl', 'rb'))

# Define feature names as per the dataset
feature_names = [
    'LIMIT_BAL', 'SEX', 'EDUCATION', 'MARRIAGE', 'AGE', 'PAY_1',
    'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6', 'BILL_AMT1', 'BILL_AMT2',
    'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6', 'PAY_AMT1',
    'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6'
]

# Define labels for display
display_labels = {
    'LIMIT_BAL': 'Credit Limit',
    'PAY_1': 'Month1 - Payment Status',
    'PAY_2': 'Month2 - Payment Status',
    'PAY_3': 'Month3 - Payment Status',
    'PAY_4': 'Month4 - Payment Status',
    'PAY_5': 'Month5 - Payment Status',
    'PAY_6': 'Month6 - Payment Status',
    'BILL_AMT1': 'Month1 - Bill Amount',
    'BILL_AMT2': 'Month2 - Bill Amount',
    'BILL_AMT3': 'Month3 - Bill Amount',
    'BILL_AMT4': 'Month4 - Bill Amount',
    'BILL_AMT5': 'Month5 - Bill Amount',
    'BILL_AMT6': 'Month6 - Bill Amount',
    'PAY_AMT1': 'Month1 - Payment Amount',
    'PAY_AMT2': 'Month2 - Payment Amount',
    'PAY_AMT3': 'Month3 - Payment Amount',
    'PAY_AMT4': 'Month4 - Payment Amount',
    'PAY_AMT5': 'Month5 - Payment Amount',
    'PAY_AMT6': 'Month6 - Payment Amount',
}

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
            label = display_labels.get(name, name)
            if name == 'SEX':
                value = st.selectbox(label, options=[''] + list(sex_options.values()), index=0)
                value = [key for key, val in sex_options.items() if val == value][0] if value else 0
            elif name == 'EDUCATION':
                value = st.selectbox(label, options=[''] + list(education_options.values()), index=0)
                value = [key for key, val in education_options.items() if val == value][0] if value else 0
            elif name == 'MARRIAGE':
                value = st.selectbox(label, options=[''] + list(marriage_options.values()), index=0)
                value = [key for key, val in marriage_options.items() if val == value][0] if value else 0
            elif name.startswith('PAY_AMT'):
                value = st.number_input(label, value=None, format="%f", step=1.0)
                value = value if value is not None else 0.0
            elif name.startswith('PAY_'):
                value = st.selectbox(label, options=[''] + list(pay_options.values()), index=0)
                value = [key for key, val in pay_options.items() if val == value][0] if value else 0
            elif name.startswith('BILL_AMT'):
                value = st.number_input(label, value=None, format="%f", step=1.0)
                value = value if value is not None else 0.0
                bill_amts.append(value)
            else:
                value = st.number_input(label, value=None, format="%f", step=1.0)
                value = value if value is not None else 0.0
            feature_values.append(value)
    if row == input_rows[0]:
        st.markdown("<div style='text-align: left;'><h4>Payment Status</h4></div>", unsafe_allow_html=True)
    if row == input_rows[1]:
        st.markdown("<div style='text-align: left;'><h4>Bill Amount</h4></div>", unsafe_allow_html=True)
    if row == input_rows[2]:
        st.markdown("<div style='text-align: left;'><h4>Payment Amount</h4></div>", unsafe_allow_html=True)

# Calculate CHANGE_AMT1 to CHANGE_AMT5
change_amts = [bill_amts[i+1] - bill_amts[i] for i in range(5)]

# Replace BILL_AMT1 to BILL_AMT6 with CHANGE_AMT1 to CHANGE_AMT5
feature_values = feature_values[:12] + change_amts + feature_values[18:]

data = np.array(feature_values).reshape(1, -1)

st.header('   ')

col1, col2, col3, col4, col5, col6 = st.columns([1, 1, 1, 1, 1, 1])

with col3:
    if st.button('Predict Default', key='predict_button', help="Click to predict whether there will be a default."):
        # Scale the input data using the loaded scaler
        data_scaled = scaler.transform(data)

        # Predict using the loaded model
       


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

# st.markdown("<div style='text-align: center;'><h1>Credit Card Default Prediction</h1></div>", unsafe_allow_html=True)

# model = pickle.load(open('app/model.pkl', 'rb'))
# scaler = pickle.load(open('app/scaler.pkl', 'rb'))

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
#                 value = st.selectbox(name, options=[''] + list(sex_options.values()), index=0)
#                 value = [key for key, val in sex_options.items() if val == value][0] if value else 0
#             elif name == 'EDUCATION':
#                 value = st.selectbox(name, options=[''] + list(education_options.values()), index=0)
#                 value = [key for key, val in education_options.items() if val == value][0] if value else 0
#             elif name == 'MARRIAGE':
#                 value = st.selectbox(name, options=[''] + list(marriage_options.values()), index=0)
#                 value = [key for key, val in marriage_options.items() if val == value][0] if value else 0
#             elif name.startswith('PAY_AMT'):
#                 value = st.number_input(name, value=None, format="%f", step=1.0)
#                 value = value if value is not None else 0.0
#             elif name.startswith('PAY_'):
#                 value = st.selectbox(name, options=[''] + list(pay_options.values()), index=0)
#                 value = [key for key, val in pay_options.items() if val == value][0] if value else 0
#             elif name.startswith('BILL_AMT'):
#                 value = st.number_input(name, value=None, format="%f", step=1.0)
#                 value = value if value is not None else 0.0
#                 bill_amts.append(value)
#             else:
#                 value = st.number_input(name, value=None, format="%f", step=1.0)
#                 value = value if value is not None else 0.0
#             feature_values.append(value)
#     if row == input_rows[0]:
#         st.markdown("<div style='text-align: left;'><h4>Payment Status</h4></div>", unsafe_allow_html=True)
#     if row == input_rows[1]:
#         st.markdown("<div style='text-align: left;'><h4>Bill Amount</h4></div>", unsafe_allow_html=True)
#     if row == input_rows[2]:
#         st.markdown("<div style='text-align: left;'><h4>Payment Amount</h4></div>", unsafe_allow_html=True)

# # Calculate CHANGE_AMT1 to CHANGE_AMT5
# change_amts = [bill_amts[i+1] - bill_amts[i] for i in range(5)]

# # Replace BILL_AMT1 to BILL_AMT6 with CHANGE_AMT1 to CHANGE_AMT5
# feature_values = feature_values[:12] + change_amts + feature_values[18:]

# data = np.array(feature_values).reshape(1, -1)

# st.header('   ')

# col1, col2, col3, col4, col5, col6 = st.columns([1, 1, 1, 1, 1, 1])

# with col3:
#     if st.button('Predict Default', key='predict_button', help="Click to predict whether there will be a default."):
#         # Scale the input data using the loaded scaler
#         data_scaled = scaler.transform(data)

#         # Predict using the loaded model
#         prediction = model.predict(data_scaled)

#         # Display the prediction
#         result = 'Default' if prediction[0] == 1 else 'Not Default'
#         st.session_state['result'] = result

# with col4:
#     if 'result' in st.session_state:
#         st.write(f'Prediction: **{st.session_state["result"]}**')

# st.markdown("</div>", unsafe_allow_html=True)
