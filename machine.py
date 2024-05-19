import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
#HouseDF = pd.read_csv('USA_Housing.csv')
#HouseDF = pd.read_csv('C:/Users/YourUsername/Desktop/USA_Housing.csv')
HouseDF = pd.read_csv('c:/Users/lenovo/OneDrive/Documents/USA_Housing.csv')
# Display the first few rows of the dataset
print(HouseDF.head())

# Display dataset information
print(HouseDF.info())

# Display summary statistics of the dataset
print(HouseDF.describe())

# Get the column names
print(HouseDF.columns)

# Create a pairplot
sns.pairplot(HouseDF)

# Create a distribution plot for the 'Price' column
sns.distplot(HouseDF['Price'])

# Create a heatmap of the correlations in the dataset
sns.heatmap(HouseDF.corr(), annot=True)

# Define features (X) and target (y)
X = HouseDF[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
             'Avg. Area Number of Bedrooms', 'Area Population']]
y = HouseDF['Price']

# Split the data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)

# Create a Linear Regression model
from sklearn.linear_model import LinearRegression
lm = LinearRegression()

# Train the model on the training data
lm.fit(X_train, y_train)

# Print the intercept
print(lm.intercept_)

# Create a DataFrame to show the coefficients
coeff_df = pd.DataFrame(lm.coef_, X.columns, columns=['Coefficient'])
print(coeff_df)

# Make predictions on the test data
predictions = lm.predict(X_test)

# Create a scatter plot of actual vs. predicted prices
plt.scatter(y_test, predictions)
plt.show()  # Display the plot

# Create a distribution plot of the residuals
sns.distplot((y_test - predictions), bins=50)

# Evaluate the model using metrics
from sklearn import metrics
print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))
