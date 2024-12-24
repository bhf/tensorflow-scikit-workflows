from core.domain.regression.regressionPipelineResult import RegressionPipelineResult
from core.domain.regression.regressionResult import RegressionResult

def compareRegressionPipelines(modelA: RegressionPipelineResult, modelB: RegressionPipelineResult):
    """ Compare the results from 2 different regression model pipelines.
    """
    return NotImplementedError

def compareRegressionModels(modelA: RegressionResult, modelB: RegressionResult):
    """ Compare the results from 2 different regression models.
    """
    return NotImplementedError