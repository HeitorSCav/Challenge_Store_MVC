from model.checkout import Cart, Order

class CheckoutView:
    # Cabeçalho e separador para exibição de pedidos
    _HEADERS = (f"{'#':<4} {'Order ID':<12} {'Customer':<20} "
                f"{'Items':>6} {'Total':>10} {'Status':<12}")
    _SEP     = "─" * len(_HEADERS)

    # Mostra os pedidos dos clientes
    def show_orders(self, orders: list[Order]) -> None:
        print(self._HEADERS)
        print(self._SEP)
        for i, o in enumerate(orders, start=1):
            print(f"{i:<4} #{o.order_id:<11} {o.customer.name:<20} "
                  f"{len(o.items):>6} "
                  f"R${o.total():>8.2f} "
                  f"{o.status.name:<12}")
        print(self._SEP)

    # Mostra o carrinho de compras
    def show_cart(self, cart: Cart) -> None:
        print(cart)

    # Mostra o pedido do cliente
    def show_order(self, order: Order) -> None:
        print(order)

    # Mostra o status do pedido
    def show_status(self, order: Order) -> None:
        print(f"Order #{order.order_id} - Status {order.status.name}")

    # Solicita confirmação do pedido
    def confirm_prompt(self) -> bool:
        return input("Confirm order? (y/n): ").strip().lower() == "yes"