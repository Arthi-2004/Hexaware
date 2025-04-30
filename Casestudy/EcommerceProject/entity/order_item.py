class OrderItem:
    def __init__(self, order_item_id, order_id, product_id, quantity):
        self.order_item_id = order_item_id
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity

    def __repr__(self):
        return f"OrderItem(order_item_id={self.order_item_id}, order_id={self.order_id}, product_id={self.product_id}, quantity={self.quantity})"

