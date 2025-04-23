import manager.order_manager as OrderManager
class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        # Check for duplicates based on product ID or product name
        if any(p.product_id == product.product_id or p.product_name == product.product_name for p in self.products):
            raise ValueError("Product with the same ID or name already exists.")
        self.products.append(product)

    def update_product(self, product_id, new_price=None, new_stock=None, new_description=None):
        product = next((p for p in self.products if p.product_id == product_id), None)
        if not product:
            raise ValueError("Product not found.")
        if new_price is not None:
            product.price = new_price
        if new_stock is not None:
            product.stock_quantity = new_stock
        if new_description:
            product.update_product_info(description=new_description)
        return "Product information updated successfully."

    def remove_product(self, product_id):
        product = next((p for p in self.products if p.product_id == product_id), None)
        if not product:
            raise ValueError("Product not found.")
        # Check if product is referenced in existing orders before removing
        if any(order.has_product(product_id) for order in OrderManager.orders):
            raise ValueError("Cannot remove product with existing orders.")
        self.products.remove(product)

    def get_all_products(self):
        return self.products

    def search_product_by_name(self, name):
        return [product for product in self.products if name.lower() in product.product_name.lower()]
