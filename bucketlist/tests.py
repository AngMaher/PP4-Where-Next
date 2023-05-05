import unittest
from django.contrib.auth.models import User
from forms import AddBucketlistForm
from models import List



# class TestAddBucketlistForm(unittest.TestCase):
#     def test_list_content_is_required(self):
#         """
#         Test is list form is left blank when submitted
#         """
#         form = List({'title': ""})
#         self.assertFalse(form.is_valid())
#         self.assertIn('title', form.errors.keys())
#         self.assertEqual(form.errors['content'][0], 'This field is required.')


class TestTest(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
