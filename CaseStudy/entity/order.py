from datetime import datetime

class Order:
    def __init__(self, customer_id, total_price, shipping_address, order_id=None, order_date=None):
        self.order_id = order_id
        self.customer_id = customer_id
        self.total_price = total_price
        self.shipping_address = shipping_address
        self.order_date = order_date if order_date else datetime.now()

    def __repr__(self):
        return (f"Order(order_id={self.order_id}, customer_id={self.customer_id}, "
                f"order_date={self.order_date}, total_price={self.total_price}, "
                f"shipping_address={self.shipping_address})")
