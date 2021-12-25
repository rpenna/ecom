class StockCalculator:

    def calculate(self, stock_operations: list) -> int:
        quantity = 0
        for operation in stock_operations:
            if operation.out:
                quantity -= operation.quantity
            else:
                quantity += operation.quantity
        return quantity
