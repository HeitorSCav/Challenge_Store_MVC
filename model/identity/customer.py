from model.identity import Person, Address, Contact

class Customer(Person):
    def __init__(self, customer_id: str, name: str, address: Address, contact: Contact):
        super().__init__(name, address, contact)  # Usa a inicialização da classe pai (Person)
        self._customer_id = customer_id
        self._loyalty_points = 0

    @property
    def customer_id(self):
        return self._customer_id

    # Adiciona pontos de fidelidade ao cliente
    def add_points(self, n: int) -> None:
        self._loyalty_points += n
    
    def __repr__(self):
        '''
        O que será que esse !r faz aqui? 
        !r chama a função repr() do objeto, que é usada para obter 
        uma representação "oficial" do objeto, geralmente útil para depuração.
        '''
        return (f"Customer(id={self._customer_id!r}, "
                f"name={self._name!r}, "
                f"address={self._address!r}, "
                f"contact={self._contact!r})")

    def __str__(self):
        return (f"[{self._customer_id}] {self._name}\n"
                f"  {self._address}\n"
                f"  {self._contact}")