# Analysis of candidates on presidential elections in Ukraine, 2014
# 23 candidates overall

import pandas as pd
import numpy as np
from ggplot import *
import matplotlib.pyplot as plt

cand = pd.read_csv("candidates.csv")

birthmean = np.mean(cand.BirthYear)
agemean = np.mean(cand.Age)
wordsmean = np.mean(cand.ProgramWords)
incomemean = np.mean(cand.IncomeTogether2013)

liveplaces = cand.Lives.value_counts()
workplaces = cand.Works.value_counts()
parties = cand.Party.value_counts()

work2 = workplaces[workplaces>1]
work3 = pd.DataFrame({'Works': work2.index, 'n':work2})
lives2 = liveplaces[liveplaces>1]

income2013comp = cand.IncomeTogether2013[cand.IncomeTogether2011>0]
income2011comp = cand.IncomeTogether2011[cand.IncomeTogether2011>0]
income2013_11_comp = income2013comp - income2011comp

age = cand.Age
agemin = age.min()
agemax = age.max()
agemedian = age.median()
agemean = age.mean()

income = cand.IncomeTogether2013
incomemin = income.min()
incomemax = income.max()
incomemedian = income.median()
incomemean = income.mean()

agehist = ggplot(aes(x="Age"), data=cand) + geom_histogram() + ggtitle("Candidates' age") + labs("Age", "Frequency")
workhist = ggplot(aes(x="Works"), data=work3) + geom_histogram()

age3 = pd.DataFrame({"Name":cand.Name, "Age": cand.Age})
age3 = age3.reindex(index = cand.Name)
