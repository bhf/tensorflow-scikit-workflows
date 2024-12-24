from dataclasses import dataclass

from core.domain.regression.regressionResult import RegressionResult

@dataclass
class RegressionPipelineResult:
    trainingRegression: RegressionResult
    testRegression: RegressionResult
    mse: float
    r2: float

