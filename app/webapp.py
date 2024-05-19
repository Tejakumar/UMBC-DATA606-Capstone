import streamlit as st

css_code = """
<style>
html, body, [class*="View"] {
    margin: 0px !important;
    padding: 0px !important;
}
.stApp {
    background-image: url("https://github.com/tejapeddi1/UMBC-DATA606-Capstone/blob/main/app/bg_img.png?raw=true");
    background-size: full;
    background-position: center;
    background-repeat: no-repeat;
}
</style>
"""
st.markdown(css_code, unsafe_allow_html=True)


# import streamlit as st
# import pickle
# import numpy as np

# model = pickle.load(open('app/model.pkl', 'rb'))
# scaler = pickle.load(open('app/scaler.pkl', 'rb'))

# # Initialize session state variables
# if 'page' not in st.session_state:
#     st.session_state.page = 0

# if 'feature_values' not in st.session_state:
#     st.session_state.feature_values = [0] * 23

# if 'bill_amts' not in st.session_state:
#     st.session_state.bill_amts = [0] * 6

# # Add background image
# page_bg_img = """
# <style>
# body {
# background-image: url("https://github.com/tejapeddi1/UMBC-DATA606-Capstone/blob/main/app/bg_img.png?raw=true");
# background-size: cover;
# }
# </style>
# """

# st.markdown(page_bg_img, unsafe_allow_html=True)

# ##st.markdown("<div style='text-align: center;'><h1>Credit Card Default Prediction</h1></div>", unsafe_allow_html=True)

# # Define feature names as per the dataset
# feature_names = [
#     'LIMIT_BAL', 'SEX', 'EDUCATION', 'MARRIAGE', 'AGE', 'PAY_1',
#     'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6', 'BILL_AMT1', 'BILL_AMT2',
#     'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6', 'PAY_AMT1',
#     'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6'
# ]

# # Pages definition
# pages = [
#     feature_names[:5],
#     feature_names[5:11],
#     feature_names[11:17],
#     feature_names[17:23]
# ]

# # Mapping for dropdown options
# sex_options = {1: 'male', 2: 'female'}
# education_options = {1: 'graduate school', 2: 'university', 3: 'high school', 4: 'others'}
# marriage_options = {1: 'married', 2: 'single', 3: 'divorce'}
# pay_options = {-2: 'No transactions', -1: 'Paid in full', 0: 'Minimum due paid', 
#                1: '1 month delay', 2: '2 months delay', 3: '3 months delay', 
#                4: '4 months delay', 5: '5 months delay', 6: '6 months delay', 
#                7: '7 months delay', 8: '8 months delay'}

# # Function to handle user input
# def handle_input(page_idx):
#     cols = st.columns(1)  # Adjust the number of columns as needed for better spacing
#     for i, name in enumerate(pages[page_idx]):
#         col = cols[i % len(cols)]
#         with col:
#             idx = feature_names.index(name)
#             if name == 'SEX':
#                 value = st.selectbox(name, options=[''] + list(sex_options.values()), index=0)
#                 value = [key for key, val in sex_options.items() if val == value][0] if value else None
#             elif name == 'EDUCATION':
#                 value = st.selectbox(name, options=[''] + list(education_options.values()), index=0)
#                 value = [key for key, val in education_options.items() if val == value][0] if value else None
#             elif name == 'MARRIAGE':
#                 value = st.selectbox(name, options=[''] + list(marriage_options.values()), index=0)
#                 value = [key for key, val in marriage_options.items() if val == value][0] if value else None
#             elif name.startswith('PAY_AMT'):
#                 value = st.number_input(name, value=None, format="%f")
#             elif name.startswith('PAY_'):
#                 value = st.selectbox(name, options=[''] + list(pay_options.values()), index=0)
#                 value = [key for key, val in pay_options.items() if val == value][0] if value else None
#             elif name.startswith('BILL_AMT'):
#                 value = st.number_input(name, value=None, format="%f")
#                 st.session_state.bill_amts[idx - 11] = value
#             else:
#                 value = st.number_input(name, value=None, format="%f")
#             st.session_state.feature_values[idx] = value

# # Handle navigation
# if st.session_state.page < len(pages) - 1:
#     handle_input(st.session_state.page)
#     if st.button('Next'):
#         st.session_state.page += 1
# else:
#     handle_input(st.session_state.page)
#     if st.button('Predict Default', key='predict_button', help="Click to predict whether there will be a default."):
#         # Calculate CHANGE_AMT1 to CHANGE_AMT5
#         change_amts = [st.session_state.bill_amts[i+1] - st.session_state.bill_amts[i] for i in range(5)]

#         # Replace BILL_AMT1 to BILL_AMT6 with CHANGE_AMT1 to CHANGE_AMT5
#         final_feature_values = st.session_state.feature_values[:12] + change_amts + st.session_state.feature_values[18:]

#         data = np.array(final_feature_values).reshape(1, -1)

#         # Scale the input data using the loaded scaler
#         data_scaled = scaler.transform(data)

#         # Predict using the loaded model
#         prediction = model.predict(data_scaled)

#         # Display the prediction
#         result = 'Default' if prediction[0] == 1 else 'Not Default'
#         st.write(f'Prediction: **{result}**')

#     if st.button('Back'):
#         st.session_state.page -= 1
