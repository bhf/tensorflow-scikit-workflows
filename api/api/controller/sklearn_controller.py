from typing import List

from api.dto.RegressionResultDTO import RegressionResultDto
from sklearnworkflows.regression.SimpleLinearRegression import SimpleLinearRegression


class SklearnController:

    def get_ols_result(self) -> RegressionResultDto:
        r = SimpleLinearRegression("OLS")
        x = [[0], [1], [2]]
        y = [0, 1, 2]
        result = r.doRegression(x,y)
        return RegressionResultDto(coefficient=str(result.coefficient), intercept=str(result.intercept))

