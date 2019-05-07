import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
data=pd.read_csv("sample.csv")
x=data['x'].values
y=data['y'].values
n=len(x)
xmean=sum(x)/len(x)
ymean=sum(y)/len(y)
print(xmean,ymean)
for i in range(n):
    beta=(sum([(x[i]-xmean)*(y[i]-ymean)])/(sum([(x[i]-xmean)**2])))
print(beta)
alpha=ymean-beta*xmean
print(alpha)
for x1 in x:
    regr=((alpha*x1)+beta)
print(regr)
plt.scatter(x,y,color='red')
plt.plot(x,regr)
plt.show()
