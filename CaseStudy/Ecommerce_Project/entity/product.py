class Product:
    def __init__(self, product_id, name, price, description, stockQuantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.description = description
        self.stockQuantity = stockQuantity  # Match the column name from the database
