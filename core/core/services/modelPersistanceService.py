from core.domain.regressionPipelineResult import RegressionPipelineResult
from core.domain.regressionResult import RegressionResult

def persistRegressionPipeline(model: RegressionPipelineResult):
    """ Persist a RegressionPipelineResult.
    """
    return NotImplementedError

def persistRegressionResult(model: RegressionResult):
    """ Persist a RegressionResult.
    """
    return NotImplementedError