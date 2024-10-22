# Implementing Neural Networks from Scratch 
# g(z)= 1 / 1 + exp(-z)
# z = w.x + b
# Gradient Decent Algorithms : 
# 1]  w = w - learning_rate*(dJ/dw)
# 2] b = b - learning_rate*(dj/db)
# J(y,y^) = 1/2m * sum (f(x)-y)^2

# For sake of simplicity we will be generating some random weights first and then wil be building on the gradient descent algo

import numpy as np 


def sigmoid(w,x,b):
    z = np.dot(w,x)+b
    return 1 / (np.exp(-z) + 1)


def weight(input):
    length=input.shape[1]
    w=np.random.randn(length).reshape(1,-1)
    b=np.random.randn(1)
    return w,b



def layer(units,label,input):
    # Input from the previous layer or the feature vector
    # Creating an Empty vector having the size same as that of number of units in the givern layer to store the output
    output = np.empty(input.shape[1])
    label=label
    for i in range(units):
        a= sigmoid(weight(input)[0],input,weight(input)[1])
        output.append(a)


# Joining all the layers together : 
def sequential(list,x):
    # combining all the layers together : 
    a=0
    for i in range(len(list)):
        if(i==0):
            a=list(i)(input=x)
        else:
            a=list(i)(input=a)

    return a



sample_input = np.random.rand(10).reshape(1,-1)

sequential(
   [layer(label='First',units=3,input=sample_input),layer(label='Second',units=2)] , x=sample_input
)
               


# ===================================================================================================================================================
# Using Class Method Approach 
