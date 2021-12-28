from django.test import TestCase

from store.models import Category, Product


# Create your tests here.
class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(
            name='Mouse Pad', slug='mouse-pad')

    def test_category_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Category))
