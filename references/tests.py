from django.test import TestCase
from .models import Reference


class ReferenceModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Reference.objects.create(
            ref='cocktail', name='MOJITO', description='Mojito is a traditional Cuban highball.')

    def test_ref_content(self):
        reference = Reference.objects.get(id=1)
        expected_object_name = f'{reference.ref}'
        self.assertEquals(expected_object_name, 'cocktail')

    def test_name_content(self):
        reference = Reference.objects.get(id=1)
        expected_object_name = f'{reference.name}'
        self.assertEquals(expected_object_name, 'MOJITO')

    def test_description_content(self):
        reference = Reference.objects.get(id=1)
        expected_object_name = f'{reference.description}'
        self.assertEquals(expected_object_name,
                          'Mojito is a traditional Cuban highball.')
