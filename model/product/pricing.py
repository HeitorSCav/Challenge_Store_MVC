from abc import ABC, abstractmethod

# Define a política de precificação para produtos
class PricingPolicy(ABC):
    @abstractmethod
    def factor(self) -> float: ...

# Define a política de precificação normal, sem desconto
class Normal(PricingPolicy):
    def factor(self):
        return 1.0

# Define a política de precificação com desconto
class Discount(PricingPolicy):
    def __init__(self, percentage: float):
        self._factor = 1.0 * percentage
    
    def factor(self):
        return self._factor