from dataclasses import dataclass

from core.domain.regressionResult import RegressionResult

@dataclass
class RegressionPipelineResult:
    trainingRegression: RegressionResult
    testRegression: RegressionResult
    mse: float
    r2: float

