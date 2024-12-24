from core.domain.classification.classificationResult import ClassificationResult
from core.interfaces.classification.IClassificationPipeline import ClassificationPipeline
class SimpleClassification(ClassificationPipeline):
    """ Encapsulate logic around classification using Tensorflow.
    """

    def __init__(self, name):
        self.name = name

    def doClassification() -> ClassificationResult:
        return NotImplementedError