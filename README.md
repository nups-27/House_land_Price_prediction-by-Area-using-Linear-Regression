# House_land_Price_prediction-by-Area-using-Linear-Regression

This project implements a linear regression model to predict property prices based on area size. The model is trained using a dataset that contains area (in square feet) as the independent variable and price (in rupees) as the dependent variable. By analyzing the relationship between these two factors, the model helps estimate property prices for given area sizes.

Project Workflow:
Data Loading & Exploration: The dataset is read using pandas from a CSV file (Book1.csv) and printed for analysis.

Data Visualization: A scatter plot is created using matplotlib to visualize the relationship between area and price.

Model Training: A Linear Regression model from scikit-learn is trained using the dataset, mapping Area as the input feature and Price as the target variable.

Regression Coefficients: The model computes the regression coefficient (slope) and intercept, which define the best-fit line equation.

Price Prediction: Using the trained model, predictions are made for new area values, such as 3,800 sq ft, to estimate the corresponding property price.

Technologies Used:
Pandas – For data handling and preprocessing.

Matplotlib & Seaborn – For data visualization and exploratory analysis.

Scikit-learn (Linear Regression) – For training the machine learning model.

Key Outcomes:
Developed a predictive model that estimates property prices based on area.

Identified the correlation between property size and price using visualization techniques.

Trained a linear regression model that generalizes well for unseen data points.

Enabled real-estate price forecasting, assisting buyers, sellers, and investors in decision-making.
