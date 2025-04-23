class Inventory:
    def __init__(self, inventoryid=None, productid=None, quantityinstock=None, laststockupdate=None):
        self.inventoryid = inventoryid
        self.productid = productid
        self.quantityinstock = quantityinstock
        self.laststockupdate = laststockupdate

    def update_inventory(self, db_connector):
        try:
            db_connector.cursor.execute("""
                UPDATE inventory
                SET quantityinstock = ?, laststockupdate = ?
                WHERE productid = ?
            """, self.quantityinstock, self.laststockupdate, self.productid)
            db_connector.connection.commit()
            print("Inventory updated successfully.")
        except Exception as e:
            print(f"Error updating inventory: {e}")

    def retrieve(self, db_connector):
        try:
            db_connector.cursor.execute("""
                SELECT * FROM inventory WHERE productid = ?
            """, self.productid)
            inventory = db_connector.cursor.fetchone()
            if inventory:
                print(inventory)
            else:
                print("Inventory not found.")
        except Exception as e:
            print(f"Error retrieving inventory: {e}")

    def retrieve_all(self, db_connector):
        try:
            db_connector.cursor.execute("SELECT * FROM inventory")
            inventories = db_connector.cursor.fetchall()
            for inventory in inventories:
                print(inventory)
        except Exception as e:
            print(f"Error retrieving inventory: {e}")
