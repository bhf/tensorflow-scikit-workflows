from typing import List

from pydantic import BaseModel

class RegressionResultDto(BaseModel):
    coefficient: str
    intercept: str