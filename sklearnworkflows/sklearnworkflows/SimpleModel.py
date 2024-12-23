from sklearnworkflows.regression.SimpleLinearRegression import SimpleLinearRegression

r = SimpleLinearRegression("OLS")
x = [[0], [1], [2]]
y = [0, 1, 2]
result = r.doRegression(x,y)
print(result.intercept)
print(result.coefficient)
print(result)