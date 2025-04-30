import unittest
from unittest.mock import patch, MagicMock
from dao.product_dao import ProductDAO
from dao.cart_dao import CartDAO
from dao.order_dao import OrderDAO
from exception.not_found_exception import NotFoundException


class EcommerceTestCase(unittest.TestCase):

    @patch('dao.product_dao.create_connection')
    def test_create_product_success(self, mock_create_connection):
        # Arrange
        mock_conn = MagicMock()
        mock_create_connection.return_value = mock_conn
        product_dao = ProductDAO()

        # Act
        product_dao.add_product('Product1', 10.0, 'Description of Product1', 100)

        # Assert
        mock_conn.cursor.return_value.execute.assert_called_once()
        mock_conn.commit.assert_called_once()

    @patch('dao.cart_dao.create_connection')
    def test_add_to_cart_success(self, mock_create_connection):
        # Arrange
        mock_conn = MagicMock()
        mock_create_connection.return_value = mock_conn
        cart_dao = CartDAO()

        # Act
        cart_dao.add_cart(1, 1, 2)

        # Assert
        mock_conn.cursor.return_value.execute.assert_called_once()
        mock_conn.commit.assert_called_once()

    @patch('dao.order_dao.create_connection')
    def test_add_order_success(self, mock_create_connection):
        # Arrange
        mock_conn = MagicMock()
        mock_create_connection.return_value = mock_conn
        order_dao = OrderDAO()

        # Act
        order_dao.add_order(1, 100.0, "123 Street")

        # Assert
        mock_conn.cursor.return_value.execute.assert_called_once()
        mock_conn.commit.assert_called_once()

    @patch('dao.product_dao.create_connection')
    def test_get_product_by_invalid_id_raises_exception(self, mock_create_connection):
        # Arrange
        mock_conn = MagicMock()
        mock_conn.cursor.return_value.fetchone.return_value = None
        mock_create_connection.return_value = mock_conn
        product_dao = ProductDAO()

        # Act + Assert
        with self.assertRaises(NotFoundException):
            product_dao.get_product_by_id(999)

    @patch('dao.cart_dao.create_connection')
    def test_view_cart_empty_raises_exception(self, mock_create_connection):
        # Arrange
        mock_conn = MagicMock()
        mock_conn.cursor.return_value.fetchall.return_value = []
        mock_create_connection.return_value = mock_conn
        cart_dao = CartDAO()

        # Act + Assert
        with self.assertRaises(NotFoundException):
            cart_dao.view_cart(1)

    @patch('dao.order_dao.create_connection')
    def test_get_order_by_invalid_customer_id_raises_exception(self, mock_create_connection):
        # Arrange
        mock_conn = MagicMock()
        mock_conn.cursor.return_value.fetchall.return_value = []
        mock_create_connection.return_value = mock_conn
        order_dao = OrderDAO()

        # Act + Assert
        with self.assertRaises(NotFoundException):
            order_dao.get_order_by_customer_id(123)

if __name__ == '__main__':
    unittest.main()
