from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from core.domain.regressionPipelineResult import RegressionPipelineResult
from core.domain.regressionResult import RegressionResult

class SimpleLinearRegression:
    """ Encapsulate logic around linear regressions.
    """

    def __init__(self, name):
        self.name = name

    def doRegression(self,X,Y):
        """ Do a simple linear regression using X and Y.
        """
        reg = linear_model.LinearRegression()
        reg.fit(X,Y)
        intercept = reg.intercept_
        coefficient = reg.coef_
        return RegressionResult(intercept, coefficient)
    
    def doRegressionPipeline(self, train_x, train_y, test_x, test_y):
        """ Run a regression pipeline that involves calculating the MSE, R2
            and returning a RegressionPipelineResult that includes the train 
            and test RegressionResult.
        """
        reg = linear_model.LinearRegression()
        reg.fit(train_x,train_y)
        
        trainingIntercept = reg.intercept_
        trainingCoefficient = reg.coef_

        testingPredictions = reg.predict(test_x)
        mse = mean_squared_error(test_y, testingPredictions)
        r2 = r2_score(test_y, testingPredictions)

        testReg = linear_model.LinearRegression()
        testReg.fit(test_x, test_y)
        testIntercept = reg.intercept_
        testCoefficient = reg.coef_

        trainingRegressionResult = RegressionResult(trainingIntercept, trainingCoefficient)
        testRegressionResult = RegressionResult(testIntercept, testCoefficient)

        return RegressionPipelineResult(trainingRegression=trainingRegressionResult, testRegression=testRegressionResult, mse=mse, r2=r2)
        