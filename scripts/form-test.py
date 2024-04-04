from django.test import TestCase
from myapp.forms import MyForm

class MyFormTestCase(TestCase):
    def test_valid_form(self):
        form_data = {'name': 'Test Name', 'email': 'test@example.com'}
        form = MyForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {'name': 'Test Name', 'email': 'invalid_email'}
        form = MyForm(data=form_data)
        self.assertFalse(form.is_valid())