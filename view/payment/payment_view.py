from model.payment import Receipt

class PaymentView:
    # Mostra os métodos de pagamento disponíveis
    def show_methods(self) -> None:
        print("Payment methods: [1] Cash  [2] Card  [3] Pix")

    # Mostra o recibo de pagamento
    def show_receipt(self, receipt: Receipt) -> None:
        print(receipt)

    # Mostra o valor total a ser pago
    def show_total(self, amount: float) -> None:
        print(f"  Total due: R$ {amount:.2f}")

    # Solicita ao usuário que escolha um método de pagamento
    def prompt_method(self) -> str:
        return input("Choose method (1/2/3): ").strip()