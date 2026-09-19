from model.identity import Customer

class CustomerView:
    # Mostra os dados de um cliente
    def show(self, customer: Customer) -> None:
        print(customer)

    # Mostra os dados de uma lista de clientes
    def show_list(self, customers: list[Customer]) -> None:
        for customer in customers:
            print(customer)

    # Mostra os dados de um cliente em formato de um dicioanário
    def prompt_data(self) -> dict:
        return {
            "name": input("Name: "),
            "email": input("Email: "),
            "phone": input("Phone: "),
            "street": input("Street: "),
            "city": input("City: "),
            "zip_code": input("ZIP: "),
        }
