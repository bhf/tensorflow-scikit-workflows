from core.domain.regression.regressionPipelineResult import RegressionPipelineResult
from core.domain.regression.regressionResult import RegressionResult

class RegressionPipeline:
    """ Encapsulate logic around linear regressions using SKLearn.
    """
    
    def doRegression(self,X,Y) -> RegressionResult:
        """ Do a simple linear regression using X and Y.
        """
        pass

    def doRegressionPipeline(self, train_x, train_y, test_x, test_y) -> RegressionPipelineResult:
        """ Run a regression pipeline that involves calculating the MSE, R2
            and returning a RegressionPipelineResult that includes the train 
            and test RegressionResult.
        """
        pass