import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd

#  Null Hypothesis: The United States GDP is on average with the other countries reported.
#  Null Hypothesis: The United States life expectancy is on average with other countries reported.
# Alternative hypothesis: There is a difference between the United States and other countries with their GDP.
# Alternative hypothesis: There is a difference between the United States and other countries with their life expectancy.

pd.set_option("display.max_columns", 100)
df = pd.read_csv(r"E:\Python Projects\Life-Expectancy-and-GDP-Starter\all_data.csv")
life_expectancy_pivot_table = pd.crosstab(df.Country, df["Life expectancy at birth (years)"])

life_tukey_results = pairwise_tukeyhsd(df["Life expectancy at birth (years)"], df.Country, 0.05)
gdp_tukey_results = pairwise_tukeyhsd( df.GDP, df.Country, 0.05)
# From the data provided, there is a difference between the United States GDP and other countries. The GDP's p-value between The United States and other countries was at 0.001, which is less than the 95% confidence interval (0.05 p-value). The null hypothesis can be rejected and the alternative hypothesis can be accepted. However for life expectancy, there is a difference for some countries. Those countries are Zimbabwe, and China with a p-value of 0.001. The other countries have a p-values ranging from 0.11 to 0.90. Those countries are Mexico at 0.1179, Germany at 0.5066, and Chile at 0.90 p-value. The null hypothesis would have to be accepted for those three countries, stating that the United States is on average with other countries for life expectancy.

# GDP bar plot
sns.set_style("darkgrid")
ax = sns.barplot(data=df, x=df.Country, y=df.GDP)
ax.set_title("Countries Gross Domestic Product (GDP)")
ax.set_ylabel("GDP in Tens of Trillions (USD)")

plt.clf()
ax2 = sns.barplot(data=df, x=df.Country, y= df["Life expectancy at birth (years)"])
ax2.set_ylabel("Years")
ax2.set_title("Countries Life Expectancy")

# Life Expectancy bar plot
us_life = df["Life expectancy at birth (years)"][df.Country == "United States of America"]
china_life = df["Life expectancy at birth (years)"][df.Country == "China"]
chile_life = df["Life expectancy at birth (years)"][df.Country == "Chile"]
mexico_life = df["Life expectancy at birth (years)"][df.Country == "Mexico"]
germany_life = df["Life expectancy at birth (years)"][df.Country == "Germany"]
zimbabwe_life = df["Life expectancy at birth (years)"][df.Country == "Zimbabwe"]
overall_life = df["Life expectancy at birth (years)"]

# GDP
china_gdp = df.GDP[df.Country == "China"]
chile_gdp = df.GDP[df.Country == "Chile"]
germany_gdp = df.GDP[df.Country == "Germany"]
mexico_gdp = df.GDP[df.Country == "Mexico"]
us_gdp = df.GDP[df.Country == "United States of America"]
zimbabwe_gdp = df.GDP[df.Country == "Zimbabwe"]
overall_gdp = df.GDP
years = df.Year[df.Country == "Chile"]
x_labels = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15"]

fstat, pval = f_oneway(china_gdp, chile_gdp, germany_gdp, mexico_gdp, us_gdp, zimbabwe_gdp)
# ANOVA for GDP shows a p-value of 1.0177777153618003e-41, which shows a significant difference.
fstat2, pval2 = f_oneway(china_life, chile_life, germany_life, mexico_life, us_life, zimbabwe_life)
# ANOVA for life expectancy shows a p-value of 7.885135700050126e-55, which shows a significant difference.

#  Null Hypothesis: There is no correlation between GDP and life expectancy with each country.
# Alternative Hypothesis: There is a correlation between GDP and life expectancy with each country.
ttest, pval3 = ttest_ind(overall_life, overall_gdp)
# After running a two-sample t-test with a p-value of 0.05, the null hypothesis can be rejected and the alternative hypothesis can be accepted. The p-value that was found was 7.007737118375318e-12, which is under the 0.05 value of significance.

# Life expectancy line graph
plt.subplot(2, 3, 1)
plt.plot(range(len(years)), chile_life)
plt.xticks(range(len(years)), labels=x_labels)
plt.suptitle("Life Expectancy Over the Years")
plt.title("Chile")
plt.ylabel("Age")

plt.subplot(2, 3, 2)
plt.plot(range(len(years)), china_life, color="orange")
plt.xticks(range(len(years)), labels=x_labels)
plt.title("China")

plt.subplot(2, 3, 3)
plt.plot(range(len(years)), germany_life, color="green")
plt.xticks(range(len(years)), labels=x_labels)
plt.title("Germany")

plt.subplot(2, 3, 4)
plt.plot(range(len(years)), mexico_life, color="red")
plt.xticks(range(len(years)), labels=x_labels)
plt.title("Mexico")
plt.xlabel("Years: 2000-2015")
plt.ylabel("Age")

plt.subplot(2, 3, 5)
plt.plot(range(len(years)), us_life, color="purple")
plt.xticks(range(len(years)), labels=x_labels)
plt.title("United States")
plt.xlabel("Years: 2000-2015")

plt.subplot(2, 3, 6)
plt.plot(range(len(years)), zimbabwe_life, color="brown")
plt.xticks(range(len(years)), labels=x_labels)
plt.title("Zimbabwe")
plt.xlabel("Years: 2000-2015")
plt.tight_layout()

# GDP line graph
plt.clf()
plt.subplot(2, 3, 1)
plt.plot(range(len(years)), chile_gdp)
plt.xticks(range(len(years)), labels=x_labels)
plt.suptitle("Gross Domestic Product Over the Years")
plt.title("Chile")
plt.ylabel("GDP in Trillions (USD)")

plt.subplot(2, 3, 2)
plt.plot(range(len(years)), china_gdp, color="orange")
plt.xticks(range(len(years)), labels=x_labels)
plt.title("China")
plt.ylabel("GDP in Tens of Trillions (USD)")

plt.subplot(2, 3, 3)
plt.plot(range(len(years)), germany_gdp, color="green")
plt.xticks(range(len(years)), labels=x_labels)
plt.title("Germany")
plt.ylabel("GDP in Trillions (USD)")

plt.subplot(2, 3, 4)
plt.plot(range(len(years)), mexico_gdp, color="red")
plt.xticks(range(len(years)), labels=x_labels)
plt.title("Mexico")
plt.xlabel("Years: 2000-2015")
plt.ylabel("GDP in Trillions (USD)")

plt.subplot(2, 3, 5)
plt.plot(range(len(years)), us_gdp)
plt.xticks(range(len(years)), labels=x_labels, color="purple")
plt.title("United States")
plt.xlabel("Years: 2000-2015")
plt.ylabel("GDP In Tens of Trillions (USD)")

plt.subplot(2, 3, 6)
plt.plot(range(len(years)), zimbabwe_gdp, color="brown")
plt.xticks(range(len(years)), labels=x_labels)
plt.title("Zimbabwe")
plt.xlabel("Years: 2000-2015")
plt.ylabel("GDP in Billions (USD)")
plt.tight_layout()

# Life Expectancy and GDP scatter plot
plt.clf()
plt.subplot(2, 3, 1)
plt.scatter(chile_life, chile_gdp)
plt.title("Chile")
plt.suptitle("Life Expectancy and GDP")
plt.ylabel("GDP in Trillions (USD)")

plt.subplot(2, 3, 2)
plt.scatter(china_life, china_gdp, color="orange")
plt.title("China")
plt.ylabel("GDP in Tens Trillions (USD)")

plt.subplot(2, 3, 3)
plt.scatter(germany_life, germany_gdp, color="green")
plt.title("Germany")
plt.ylabel("GDP in Trillions (USD)")

plt.subplot(2, 3, 4)
plt.scatter(mexico_life, mexico_gdp, color="red")
plt.title("Mexico")
plt.xlabel("Life Expectancy")
plt.ylabel("GDP in Trillions (USD)")

plt.subplot(2, 3, 5)
plt.scatter(us_life, us_gdp, color="purple")
plt.title("United States")
plt.xlabel("Life Expectancy")
plt.ylabel("GDP in Tens Trillions (USD)")

plt.subplot(2, 3, 6)
plt.scatter(zimbabwe_life, zimbabwe_gdp, color="brown")
plt.title("Zimbabwe")
plt.xlabel("Life Expectancy")
plt.ylabel("GDP in Billions (USD)")
plt.tight_layout()

# Conclusion: From the data provided and the hypotheses that were drawn, there seems to be a correlation between GDP and life expectancy between all countries. The bar graph showed that Germany had the highest life expectancy, and Zimbabwe had the lowest. For GDP, the United States of America had the highest and once again Zimbabwe had the lowest. A two-sample t test was ran to verify if there was a correlation between GDP and life expectancy. There was a confidence interval (p-value) of 95% (0.05) that was indicated previous to the test. The results showed a p-value of 7.007737118375318e-12, which signified that there is a correlation between the two values. A scatter plot between the life expectancy and GDP was then created to visualize the significance. The scatter plot showed a difference, especially for Zimbabwe.
# Another hypothesis was formed to see if there is significant difference when other countries were put up aginst the United States for GDP and life expectancy. An ANOVA and Tukey(HSD) test were ran to see if there was a difference. The data provided evidence that there was a difference between the United States GDP and other countries. Every country that was ran against the U.S. in the Tukey(HSD) test showed a p-value of 0.001, and the ANOVA test showed p-value of 1.0177777153618003e-41. A bar chart was created to visualize the findings, and it showed a drastic difference if GDP. However, there was a different outcome in the hypothesis test when it came to life expectancy. The Tukey(HSD) test showed a difference in only two countries when compared to the U.S. which were Zimbabwe, and China with a p-value of 0.001. The other three countries, Chile (0.90), Germany (0.5066), and Mexico (0.1179), had higher p-values which caused an acceptance of the null hypothesis for those three. If we only used the ANOVA test for life expectancy, which gave a p-value of 7.885135700050126e-55 as the conclusive answer, and would have raised a type I error.