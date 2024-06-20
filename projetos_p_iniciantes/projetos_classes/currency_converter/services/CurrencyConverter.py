class CurrencyConverter:
    def __init__(self, current_value: float, quantity_buy: float) -> None:
        self.current_value: float = current_value
        self.quantity_buy: float = quantity_buy

    def purchase_value(self) -> float:
        return self.current_value * self.quantity_buy

    def __str__(self) -> str:
        return f"Purchace Value = {self.purchase_value()}"
