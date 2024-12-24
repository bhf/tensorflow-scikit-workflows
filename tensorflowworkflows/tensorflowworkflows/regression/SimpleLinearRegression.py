from core.domain.regression.regressionPipelineResult import RegressionPipelineResult
from core.domain.regression.regressionResult import RegressionResult
from core.interfaces.regression.IRegressionPipeline import RegressionPipeline

class SimpleLinearRegression(RegressionPipeline):
    """ Encapsulate logic around linear regressions using Tensorflow.
    """

    def __init__(self, name):
        self.name = name

    def doRegression(self,X,Y):
        return NotImplementedError
    
    def doRegressionPipeline(self, train_x, train_y, test_x, test_y):
        return NotImplementedError
        