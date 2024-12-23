from sklearn import linear_model
from core.domain.regressionResult import RegressionResult

class SimpleLinearRegression:
    def __init__(self, name):
        self.name = name

    def doRegression(self,X,Y):
        reg = linear_model.LinearRegression()
        reg.fit(X,Y)
        intercept = reg.intercept_
        coefficient = reg.coef_
        return RegressionResult(intercept, coefficient)
        