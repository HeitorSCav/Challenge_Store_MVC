from enum import Enum, auto
from uuid import uuid4
from model.checkout import Cart

class OrderStatus(Enum):
    PENDING = 1
    PAID = 2
    FULFILLED = 3
    
class Order:
    # Define as transições de status do pedido
    _TRANSITIONS = {
        OrderStatus.PENDING:   OrderStatus.PAID,
        OrderStatus.PAID:      OrderStatus.FULFILLED,
        OrderStatus.FULFILLED: OrderStatus.PENDING,
    }

    def __init__(self, cart: Cart):
        self._order_id = str(uuid4())[:8]  # uuid4() gera um identificador único, mas vamos encurtá-lo para 8 caracteres
        self._customer = cart.customer
        self._items = list(cart.items)
        self._status = OrderStatus.PENDING

    @property
    def order_id(self):
        return self._order_id
    
    @property
    def status(self):
        return self._status
    
    @property
    def items(self):
        return list(self._items)

    # Calcula o total do pedido somando os subtotais de todos os itens
    def total(self) -> float:
        return sum(i.subtotal() for i in self._items)

    # Avança o status do pedido para o próximo estado definido na transição
    def advance_status(self) -> None:
        next_status = self._TRANSITIONS[self._status]
        self._status = next_status

    def __str__(self):
        lines = "\n".join(f"  {i}" for i in self._items)
        return (f"Order #{self._order_id} [{self._status.name}]\n"
                f"  Customer: {self._customer.name}\n"
                f"{lines}\n"
                f"  Total: R$ {self.total():.2f}")

    def __repr__(self):
        return f"Order(id={self._order_id!r}, status={self._status.name})"
