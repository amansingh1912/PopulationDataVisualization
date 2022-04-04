import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df= pd.read_csv(r'C:\Users\AMAN KUMAR SINGH\Downloads\india_population.csv')
print(df.describe())


# sns.scatterplot(x='Year', y='Population', data=df, label='Population')
# sns.scatterplot(x='Year', y='Urban Population', data=df, marker='o',size=34, label='Urban Population')
# Here, it shows that "Year" and "Population" & "Year" and "Urban Population" both increase with increase in the year values.

# sns.scatterplot(x='Population', y='Urban Population', data=df)
## With the increase in Population, urban population also has increased linearly.
## Here population and urban population are positively correlated as increase in population also shows increase in urban population somewhat linearly.


sns.barplot(x='Year', y='Yearly Change', data=df)
## Graph shows that Yearly change is maximum in the span of 1995-2000.
plt.show()





