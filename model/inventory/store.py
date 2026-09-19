from model.inventory import StockItem

class Shelf:
    def __init__(self, code: str):
        self._code = code
        self._items: list[StockItem] = []

    @property
    def code(self):
        return self._code
    
    @property
    def items(self):
        return list(self._items)

    # Adiciona um item de estoque à prateleira
    def add_item(self, item: StockItem) -> None:
        self._items.append(item)

    # Encontra um item de estoque na prateleira com base no SKU do produto
    def find(self, sku: str) -> StockItem | None:
        for item in self._items:
            if str(item.product.sku) == sku:
                return item
        return None

    def __str__(self):
        return f"Shelf({self._code})"
    
    def __repr__(self):
        return f"Shelf(code={self._code!r}, items={len(self._items)})"


class Aisle:
    def __init__(self, number: int):
        self._number  = number
        self._shelves: list[Shelf] = []

    @property
    def number(self):
        return self._number
    
    @property
    def shelves(self):
        return list(self._shelves)

    # Adiciona uma prateleira ao corredor
    def add_shelf(self, shelf: Shelf) -> None:
        self._shelves.append(shelf)

    # Encontra um item de estoque em qualquer prateleira do corredor com base no SKU do produto 
    def find(self, sku: str) -> StockItem | None:
        for shelf in self._shelves:
            item = shelf.find(sku)
            if item:
                return item
        return None

    def __str__(self):
        return f"Aisle {self._number}"
    
    def __repr__(self):
        return f"Aisle(number={self._number}, shelves={len(self._shelves)})"