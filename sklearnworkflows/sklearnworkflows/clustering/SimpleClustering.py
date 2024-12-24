from core.domain.clustering.clusteringResult import ClusteringResult
from core.interfaces.clustering.IClusteringPipeline import ClusteringPipeline
class SimpleClustering(ClusteringPipeline):
    """ Encapsulate logic around clustering using SKLearn.
    """

    def __init__(self, name):
        self.name = name

    def doClustering() -> ClusteringResult:
        return NotImplementedError

