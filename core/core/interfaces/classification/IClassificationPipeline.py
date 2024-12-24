from core.domain.classification.classificationResult import ClassificationResult

class ClassificationPipeline:
    """ Encapsulate logic around classification models using SKLearn.
    """

    def __init__(self, name):
        self.name = name

    def doClassification() -> ClassificationResult:
        pass