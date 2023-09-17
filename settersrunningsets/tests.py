# Create your tests here.
from django.test import TestCase, RequestFactory
from unittest.mock import patch
from .views import settersrunningsets_view


class TestViews(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    @patch('settersrunningsets.views.create_plot')
    def test_settersrunningsets_view(self, mock_create_plot):
        # Set up the mock to return a predictable result
        mock_create_plot.return_value = "mocked_plot_data"

        # Simulate a GET request to the view
        request = self.factory.get('/your_url_path')
        response = settersrunningsets_view(request)

        self.assertEqual(response.status_code, 200)

        # Check that the response contains the plot data
        self.assertContains(response, 'mocked_plot_data')
