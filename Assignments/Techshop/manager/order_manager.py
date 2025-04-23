class OrderManager:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def get_all_orders(self):
        return self.orders

    def get_orders_sorted_by_date(self):
        return sorted(self.orders, key=lambda o: o.order_date)

    def get_orders_by_status(self, status):
        return [order for order in self.orders if order.status == status]

    def has_product(self, product_id):
        return any(any(detail.product.product_id == product_id for detail in order._Order__order_details)
                   for order in self.orders)
