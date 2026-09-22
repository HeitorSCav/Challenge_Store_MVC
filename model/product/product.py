from dataclasses import dataclass
from model.product import ProductType, PricingPolicy, Normal, Discount

# Objetos de Valor
@dataclass()
class SKU:
    code: str

    @property
    def code(self):
        return self._code

    # Valida o SKU, garantindo que não seja vazio ou apenas espaços em branco
    def __post_init__(self):
        if not self.code or not self.code.strip():
            raise ValueError("Error! SKU missing")
        self.code = self.code.strip()

    def __str__(self):
        return self.code

@dataclass()
class Price:
    amount: float

    # Valida o Price, garantindo que não seja negativo ou zero
    def __post_init__(self):
        if self.amount <= 0:
            raise ValueError("Error! Invalid price")

    def __str__(self):
        return f"R$ {self.amount:.2f}"
    

class Product:
    def __init__(self, sku: SKU, name: str, price: Price, category: ProductType, policy: PricingPolicy = None):
        self._sku = sku
        self._name = name
        self._price = price
        self._category = category
        self._policy = policy

    # Getters
    @property
    def sku(self):
        return self._sku
    
    @property
    def name(self):
        return self._name
    
    @property
    def price(self):
        return self._price
    
    @property
    def category(self):
        return self._category

    @property
    def policy(self):
        return self._policy
    
    # Setters
    @policy.setter
    def policy(self, p: PricingPolicy): 
        self._policy = p

    # Calcula o preço final do produto com base na política de precificação
    def final_price(self) -> float:
        return self._price.amount + self._policy.factor()

    def __repr__(self):
        return (f"Product(sku={self._sku!r}, name={self._name!r}, "
                f"price={self._price!r}, category={self._category.name})")

    def __str__(self):
        return (f"[{self._sku}] {self._name} "
                f"({self._category.name}) - {self._price} "
                f"\nFinal price: R$ {self.final_price():.2f}")

    def __eq__(self, other):
        return isinstance(other, Product) and self._sku == other._sku