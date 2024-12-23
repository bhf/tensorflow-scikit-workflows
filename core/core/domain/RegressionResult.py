class RegressionResult:
    def __init__(self, intercept, coefficient):
        self.coefficient = coefficient
        self.intercept = intercept

    def __str__(self):
        return str(self.intercept)+" + "+str(self.coefficient)+"x"
