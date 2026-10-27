"""Converted from regression.ipynb."""

import numpy as np
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_squared_error
import matplotlib.pyplot as plt

# (coeffecient determinant) r2_score is a regression score function to evaluate the performance of a linear regression model <br>
# amount of variable in the output dependent attribute which is predictable from the input independent variable(s)<br>
# r2=1-SS(res)/SS(total)   -->(SSres: sum of squares of the residual errors) <br>(SStotal:total sum  of errors)<br>
# best possible score of r2_score  is 1<br>
# it can be -ve (worst condt)

# actualvalue(y)  predicted(f)    error e1= y-f    e1^2(ssres)    e2=y-mean  e2^2<br>
# 10              10              0                   0           -10          100
# 20              20              0                   0            0              0
# 30              30              0                   0            10           100
# mean=20
# r2=1-(0/200)=>gives accurate result

# actualvalue(y)  predicted(f)    error e1= y-f    e1^2(ssres)    e2=y-mean  e2^2<br>
# 10              20              -10                 100         -10          100
# 20              20              0                   0            0              0
# 30              20              10                  100          10           100
# mean=20
# r2=1-(200/200)=> gives accurate result

# actualvalue(y)  predicted(f)    error e1= y-f    e1^2(ssres)    e2=y-mean  e2^2<br>
# 10              30              -20                 400         -10          100
# 20              10              10                  100           0              0
# 30              20              10                  100          10           100
# mean=20
# r2=1-(600/200)=> gives -ve ans (worst case)

# np.random.seed(42)
# random.state(42)

np.random.seed(42)
X=2*np.random.rand(100,1)
y=4+3*X+np.random.rand(100,1)

# in y np.random is added for noise

X_train,X_test,Y_train,Y_test=train_test_split(X,y,train_size=0.8,random_state=42)

m=LinearRegression()
m.fit(X_train,Y_train)
y_pred=m.predict(X_test)
se=mean_squared_error(Y_test,y_pred)
print(se)
print(r2_score(Y_test,y_pred))

plt.scatter(X,y,color='red',marker='x',label="actual")
plt.plot(X_test,y_pred,label='prediction')
plt.xlabel('X-data')
plt.ylabel('Y-data')
plt.legend()
plt.show()

n=float(input("enter value: "))
n1=np.array([[n]])
print(m.predict(n1))
