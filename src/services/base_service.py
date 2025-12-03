from abc import ABC, abstractmethod

class BaseService(ABC):
    @abstractmethod
    def list(self):
        pass
    
    @abstractmethod
    def get(self, id: int):
        pass
    
    @abstractmethod
    def create(self, **kwargs):
        pass
    
    @abstractmethod
    def update(self, id: int, **kwargs):
        pass
    
    @abstractmethod
    def delete(self, id: int):
        pass