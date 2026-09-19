from model.checkout import Order, Cart
from model.identity import Customer
from model.product import Product
from view.checkout import CheckoutView

class CheckoutController:
    def __init__(self, view: CheckoutView):
        self._cart: Cart | None = None
        self._orders: list[Order] = []
        self._view = view

    # Abre um novo carrinho de compras para o cliente especificado
    def open_cart(self, customer: Customer) -> None:
        self._cart = Cart(customer)

    # Adiciona um item ao carrinho de compras, verificando se o carrinho está aberto
    def add_item(self, product: Product, qty: int) -> None:
        if not self._cart:
            raise ValueError("No open cart")
        self._cart.add(product, qty)
        self._view.show_cart(self._cart)

    # Confirma o pedido, mostrando o carrinho e solicitando confirmação do cliente. 
    def confirm(self) -> Order | None:
        self._view.show_cart(self._cart)
        if self._view.confirm_prompt():
            print("Obrigado por comprar conosco!") 
            order = Order(self._cart)
            self._orders.append(order)
            self._view.show_order(order)
            return order
        return None

    # Avança o status do pedido, verificando se o pedido está aberto
    def advance(self) -> None:
        # TODO: Vou pra casa agora
        pass