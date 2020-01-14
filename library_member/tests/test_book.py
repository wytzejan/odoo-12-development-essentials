from odoo.tests.common import TransactionCase


class TestBook(TransactionCase):

    def setUp(self, *args, **kwargs):
        result = super().setUp(*args, **kwargs)
        user_admin = self.env.ref('base.user_admin')
        self.env = self.env(user=user_admin)
        self.Book = self.env['library.book']
        self.book_lotf = self.Book.create({
            'name': 'Lord of the Flies',
            'isbn': '0-571-05686-51234512345'
        })
        return result

    def test_create(self):
        """Test Books are active by default"""
        self.assertEqual(self.book_lotf.active, True)

    def test_check_isbn(self):
        """Check valid 10-digit ISBN"""
        self.assertTrue(self.book_lotf._check_isbn)
