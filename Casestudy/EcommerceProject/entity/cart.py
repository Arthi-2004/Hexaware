# cart.py
class Cart:
    def __init__(self, cart_id, customer_id, product_id, quantity):
        self.cart_id = cart_id
        self.customer_id = customer_id
        self.product_id = product_id
        self.quantity = quantity

    def __repr__(self):
        return f"Cart(cart_id={self.cart_id}, customer_id={self.customer_id}, product_id={self.product_id}, quantity={self.quantity})"
