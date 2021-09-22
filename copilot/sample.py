# build a sample of the data
import pandas as pd
import numpy as np

# create random data with name , age , income and IQ

names = ['name'+str(i) for i in range(100)]
# create age data random from 16 to 80 with mean of 40 and normal distribution
ages = np.random.randint(16,80,100)
# create income data random from 1000 to 10000 with mean of 5000 and normal distribution
incomes = np.random.randint(1000,10000,100)
# create IQ data random from 60 to 150 with mean of 100 and normal distribution
IQs = np.random.randint(60,150,100)
# create a dataframe
df = pd.DataFrame({'name':names,'age':ages,'income':incomes,'IQ':IQs})


# create regression model with statsmodels formula api on income ,IQ and age
import statsmodels.formula.api as smf

model = smf.ols(formula='income ~ IQ + age',data=df)
results = model.fit()
print(results.summary())

# plot the regression model
import matplotlib.pyplot as plt

plt.scatter(df['age'],df['income'])
plt.plot(df['age'],results.predict(df),color='red')
plt.title('Regression Model')
plt.xlabel('age')
plt.ylabel('income')
plt.show()