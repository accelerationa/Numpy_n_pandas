import pandas as pd
import numpy as np


df = pd.read_csv("logs-insights-results.csv")

p90 = np.percentile(np.array(df.iloc[:,2:3].values), 90)
p99 = np.percentile(np.array(df.iloc[:,2:3].values), 99)
p999 = np.percentile(np.array(df.iloc[:,2:3].values), 99.9)
avg = np.average(np.array(df.iloc[:,2:3].values))

print(avg)
print(p90)
print(p99)
print(p999)

