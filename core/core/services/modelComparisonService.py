from core.domain.regressionPipelineResult import RegressionPipelineResult
from core.domain.regressionResult import RegressionResult

def compareRegressionPipelines(modelA: RegressionPipelineResult, modelB: RegressionPipelineResult):
    """ Compare the results from 2 different regression model pipelines.
    """
    return NotImplementedError

def compareRegressionModels(modelA: RegressionResult, modelB: RegressionResult):
    """ Compare the results from 2 different regression models.
    """
    return NotImplementedError