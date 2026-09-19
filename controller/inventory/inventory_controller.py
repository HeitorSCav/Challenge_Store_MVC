from model.inventory import StockItem, Aisle, Shelf
from model.product import Product
from view.inventory import InventoryView

class InventoryController:
    def __init__(self, view: InventoryView):
        self._aisles: list[Aisle] = None
        self._view = view

    # Adiciona um novo corredor ao inventário
    def add_aisle(self, number: int) -> Aisle:
        aisle = Aisle(number)
        self._aisles.append(aisle)
        return aisle

    # Adiciona um novo item de estoque a uma prateleira específica
    def stock_item(self, shelf: Shelf, product: Product, qty: int, min_stock: int = 3) -> None:
        item = StockItem(product, qty, min_stock)
        shelf.add_item(item)
        self._view.show(item)

    # Atualiza a quantidade de um item de estoque específico
    def restock(self, sku: str, n: int) -> None:
        item = self._find(sku)
        if item:
            item.add(n)
            self._view.show(item)

    # Alerta o usuário se algum item de estoque estiver abaixo do nível mínimo
    def low_stock_report(self) -> None:
        for aisle in self._aisles:
            for shelf in aisle.shelves:
                for shelf in aisle.shelves:
                    if shelf.low_stock():
                        self._view.show_alert()

    # Encontra um item de estoque pelo SKU, percorrendo todos os corredores
    def _find(self, sku: str) -> StockItem | None:
        for aisle in self._aisles:
            item = aisle.find(sku)
            if item == sku:
                return item
        return None