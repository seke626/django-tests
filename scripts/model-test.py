from django.test import TestCase
from myapp.models import MyModel

class MyModelTestCase(TestCase):
    def setUp(self):
        MyModel.objects.create(name='Test Name', description='Test Description')

    def test_model_fields(self):
        obj = MyModel.objects.get(name='Test Name')
        self.assertEqual(obj.name, 'Test Name')
        self.assertEqual(obj.description, 'Test Description')