class SimpleLinearRegression:
    """ Encapsulate logic around linear regressions using Tensorflow.
    """

    def __init__(self, name):
        self.name = name

    def doRegression(self,X,Y):
        """ Do a simple linear regression using X and Y.
        """

        return NotImplementedError
    
    def doRegressionPipeline(self, train_x, train_y, test_x, test_y):
        """ Run a regression pipeline that involves calculating the MSE, R2
            and returning a RegressionPipelineResult that includes the train 
            and test RegressionResult.
        """
        
        return NotImplementedError
        