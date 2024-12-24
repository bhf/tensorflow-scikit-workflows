from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from core.domain.regression.regressionPipelineResult import RegressionPipelineResult
from core.domain.regression.regressionResult import RegressionResult
from core.interfaces.regression.IRegressionPipeline import RegressionPipeline

class SimpleLinearRegression(RegressionPipeline):
    """ Encapsulate logic around linear regressions using SKLearn.
    """

    def __init__(self, name):
        self.name = name

    def doRegression(self,X,Y):
        reg = linear_model.LinearRegression()
        reg.fit(X,Y)
        intercept = reg.intercept_
        coefficient = reg.coef_
        return RegressionResult(intercept, coefficient)
    
    def doRegressionPipeline(self, train_x, train_y, test_x, test_y):
        trainingSetRegression = linear_model.LinearRegression()
        trainingSetRegression.fit(train_x,train_y)
        
        trainingIntercept = trainingSetRegression.intercept_
        trainingCoefficient = trainingSetRegression.coef_

        testingSetPredictions = trainingSetRegression.predict(test_x)
        mse = mean_squared_error(test_y, testingSetPredictions)
        r2 = r2_score(test_y, testingSetPredictions)

        testSetRegression = linear_model.LinearRegression()
        testSetRegression.fit(test_x, test_y)
        testIntercept = trainingSetRegression.intercept_
        testCoefficient = trainingSetRegression.coef_

        trainingSetRegressionResult = RegressionResult(trainingIntercept, trainingCoefficient)
        testSetRegressionResult = RegressionResult(testIntercept, testCoefficient)

        return RegressionPipelineResult(trainingRegression=trainingSetRegressionResult, testRegression=testSetRegressionResult, mse=mse, r2=r2)
        