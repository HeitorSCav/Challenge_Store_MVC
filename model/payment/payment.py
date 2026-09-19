from abc import ABC, abstractmethod
from model.checkout import Order
from model.payment import Receipt
import datetime

class Payment(ABC):
    @abstractmethod
    def process(self, order: "Order") -> Receipt: ...

    def _make_receipt(self, order: "Order", method: str) -> Receipt:
        return Receipt(
            order_id = order.order_id,
            amount = order.total(),
            method = method,
            timestamp = datetime.now().strftime("dd-mm-yyyy %H:%M:%S"),
        )

class Cash(Payment):
    def __init__(self, tendered: float):
        self._tendered = tendered

# Processa o pagamento de um pedido usando dinheiro e retorna um recibo
    def process(self, order: "Order") -> None:
        # TODO: faço depois do cafézinho
        pass

class Card(Payment):
    def __init__(self, last4: str):
        self._last4 = last4

    # Processa o pagamento de um pedido usando cartão e retorna um recibo
    def process(self, order: "Order") -> None:
        # TODO: faço depois do cafézinho
        pass

class Pix(Payment):
    def __init__(self, key: str):
        self._key = key

    # Processa o pagamento de um pedido usando Pix e retorna um recibo
    def process(self, order: "Order") -> Receipt:
        receipt = self._make_receipt(order, f"Pix: {self._key}")
        order.advance_status()
        return receipt