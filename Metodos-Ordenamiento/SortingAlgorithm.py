from abc import ABC, abstractmethod

class SortingAlgorithm(ABC):
    @abstractmethod
    def sort(self, arr, key, ascending=True):
        pass