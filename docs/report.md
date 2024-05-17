
# Project Report

## Title and Author

**Project Title:** Credit Card Default Prediction  
**Prepared for:** UMBC Data Science Master Degree Capstone by Dr. Chaojie (Jay) Wang  
**Author Name** Teja Kumar Reddy Peddi  
**Github:** [Github](https://github.com/Tejakumar)  
**Linkedin:** [linkedin](https://www.linkedin.com/in/teja-peddi-462190191/)  
**Presentation:**  
**Youtube:** 

## Background

Credit card default prediction is a crucial task in the financial sector. Predicting whether a credit card holder will default on their payment allows financial institutions to manage risk effectively and make informed decisions regarding lending practices. This project aims to utilize machine learning techniques to predict credit card defaults based on various demographic and credit-related factors.

### Research Questions:

- What are the key factors influencing credit card defaults?
- Can machine learning models accurately predict credit card defaults based on historical payment and demographic data?

## Data

### Data Sources:
The dataset used for this project is sourced from the UCI Machine Learning Repository and contains information on default payments, demographic factors, credit data, and payment history of credit card clients in Taiwan from April 2005 to September 2005.

### Data Description:
- **Dataset:** [UCI_Credit_Card.csv](https://www.kaggle.com/datasets/uciml/default-of-credit-card-clients-dataset)
- **Size:** 2.86 MB
- **Number of Rows:** 30,000
- **Number of Columns:** 25

### Time Period:
April 2005 to September 2005

### Each Row Represents:
A credit card client

### Data Dictionary:

1. **ID:** ID of each client
2. **LIMIT_BAL:** Amount of given credit in NT dollars
3. **SEX:** Gender (1=male, 2=female)
4. **EDUCATION:** Level of education (1=graduate school, 2=university, 3=high school, 4=others, 5=unknown, 6=unknown)
5. **MARRIAGE:** Marital status (1=married, 2=single, 3=divorce, 0=others)
6. **AGE:** Age in years
7. **PAY_0** to **PAY_6:** Repayment status from April to September 2005(-2 = No transactions, -1 = Paid in full, 0 = Minimum due paid, 1 to 9 = No. of months delayed)
8. **BILL_AMT1** to **BILL_AMT6:** Amount of bill statement from April to September 2005 (NT Dollars)
9. **PAY_AMT1** to **PAY_AMT6:** Amount of previous payment from April to September 2005 (NT Dollars)
10. **default.payment.next.month:** Default payment indicator (1=yes, 0=no)

### Target/Label Variable:
**default.payment.next.month**

### Features/Predictors:
All other variables except ID, as they may influence the likelihood of default.

By analyzing this dataset and applying machine learning algorithms, we aim to build a predictive model that accurately identifies individuals at risk of defaulting on their credit card payments, thus assisting financial institutions in risk assessment and decision-making processes.

### Exploratory Data Analysis

