from model.inventory import StockItem

class InventoryView:
    # Mostra os detalhes de um item de estoque
    def show(self, item: StockItem) -> None:
        print(item)

    # Mostra os detalhes de uma lista de itens de estoque
    def show_list(self, items: list[StockItem]) -> None:
        for item in items:
            print(item)

    # Mostra um alerta de estoque baixo para um item específico
    def show_alert(self, item: StockItem) -> None:
        print(f"Warning! Low Stock on {item}")

    # Mostra os detalhes de um item de estoque em formato de dicionário
    def prompt_data(self) -> dict:
        return {
            "sku": input("SKU: "),
            "quantity": any(input("Quantity: ")),
            "min_stock": any(input("Min stock: ")),
            "shelf": input("Shelf code: "),
        }