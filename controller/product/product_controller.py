from model.product import PricingPolicy, Normal, Discount, Product, Price, SKU, ProductType
from view.product import ProductView

class ProductController:
    def __init__(self, view: ProductView):
        self._products: list[Product] = None
        self._view = view

    # Adiciona um novo produto à lista de produtos, solicitando os dados do produto ao usuário
    def add(self) -> Product:
        data = self._view.prompt_data()
        product = Product(
            sku = SKU(data["sku"]),
            name = data["name"],
            price = Price(data["price"]),
            category = ProductType[data["category"].upper()],
        )
        self._products.append(data)
        self._view.show(product)
        return product

    # Encontra um produto pelo SKU, mostrando os detalhes do produto encontrado
    def find(self, sku: str) -> Product | None:
        for p in self._products:
            if str(p.sku) == sku:
                self._view.show(p)
                return p
        return None

    # Aplica uma política de preço a um produto específico
    def apply_policy(self, sku: str, policy: PricingPolicy) -> None:
        product = self.find(sku)
        if product:
            product.policy = policy

    # Futura implementação 
    def prompt_choice(self) -> Product | None:
        pass