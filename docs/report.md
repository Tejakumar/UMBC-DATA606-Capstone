
# Project Report

## Title and Author

**Project Title:** Credit Card Default Prediction  
**Prepared for:** UMBC Data Science Master Degree Capstone by Dr. Chaojie (Jay) Wang  
**Author Name** Teja Kumar Reddy Peddi  
**Github:** [Github Link](https://github.com/tejapeddi1)  
**Linkedin:** [linkedin Link](https://www.linkedin.com/in/teja-peddi-462190191/)  
**Presentation:** [PPT Link](https://github.com/tejapeddi1/UMBC-DATA606-Capstone/blob/main/docs/Presentation.pdf)  
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
1. Insights on Age  
   ![](https://github.com/tejapeddi1/UMBC-DATA606-Capstone/blob/main/docs/images/2.png)  
   The age group of 30-35 years old has lowest chances for defaulting, while the highest occur at the extremes(20-25 and 60+)  
2. Insights on Gender  
   ![](https://github.com/tejapeddi1/UMBC-DATA606-Capstone/blob/main/docs/images/4.png)  
   It is observed that Men have a slightly higher chance of defaulting than women  
3. Insights on Marital Status  
   ![](https://github.com/tejapeddi1/UMBC-DATA606-Capstone/blob/main/docs/images/6.png)  
   It is observed that Single people have lower chances of defaulting than married and divorced people  
4. Insights on Education Level  
   ![](https://github.com/tejapeddi1/UMBC-DATA606-Capstone/blob/main/docs/images/8.png)  
   Considering the level of education, it seems that a higher education translates to a lower chance of default  
5. Insights of Credit Limit  
   ![](https://github.com/tejapeddi1/UMBC-DATA606-Capstone/blob/main/docs/images/lim2.png)  
   - Over 30% of default can be observed with credit limit of 50K or less
   - Also, the higher the credit limit, the lower is the chance of defaulting  
6. Insights on Previous month payment status  
   ![](https://github.com/tejapeddi1/UMBC-DATA606-Capstone/blob/main/docs/images/9.png)  
   It is observed that the likelihood of default are much lower for the people who duly paid or paying minimum due each month rather than the people who tend to delay their payment over months.

### Modelling
 - As the data was unbalanced, I have undersampled the majority class and slightly oversampled the minority class
 - Divided the data into Train test split of 80-20
 - Implemented Logistic regression, Decision Trees, Random Forest Classifier and XGBoost
 - Achieved best results with Random Forest, but found that the model is slightly overfitting
 - Implemented Hyper parameter Tuning using GridSearchCV with 5-fold Cross validation and eliminated overfitting  

**RESULTS**  
- Train Accuracy : 79.32%
- Test Accuracy : 74.25%
- Precision : 0.75
- Recall : 0.74
- F1-Score : 0.74
Accuracy: Decent accuracy of 74.25% for an imbalanced problem  
Precision, Recall, and F1-Score: The model performs better at identifying negatives (Class 0) than positives (Class 1)  

![](https://github.com/tejapeddi1/UMBC-DATA606-Capstone/blob/main/docs/images/10.png)   
Confusion Matrix Insights: There is a decent balance of values for general predictability but there is space for improvement for false negatives which can be achieved using better data

### Future Scope
- Incorporating More Data: As we know machine learning models are garbage in - garbage out, A balanced data and an adequate amount of samples of both the classes can significantly improve the model's accuracy and predictive power.
- Real-Time Prediction Systems: Developing real-time prediction capabilities will allow for instant risk assessments, enabling financial institutions to make timely and informed decisions.
- Continuous Monitoring and Recalibration: Regularly updating and recalibrating the model will ensure it remains effective and accurate in response to changing economic conditions and consumer behaviors.

### Conclusion
- The Random Forest model with tuned parameters using GridSearchCV has acheived an Accuracy of 74.25% in predicting credit card defaults using various demographic factors and previous payment histories
- Overall, the trained machine learning model offers a robust tool for financial institutions to manage credit risk effectively.
- By identifying high-risk customers through key features like payment history and credit utilization, the model enables proactive risk management and more informed lending decisions.
- This predictive capability can lead to reduced default rates and improved financial stability.
- Future enhancements and real-time implementations promise even greater accuracy and adaptability to changing economic conditions
