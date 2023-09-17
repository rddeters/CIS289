# Create your tests here.
from django.test import TestCase, RequestFactory
from unittest.mock import patch
from .views import serversfaults_view


class TestViews(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    @patch('serversfaults.views.create_plot')
    def test_serversfaults_view(self, mock_create_plot):
        # Set up the mock to return a predictable result
        mock_create_plot.return_value = "mocked_plot_data"

        # Simulate a GET request to the view
        request = self.factory.get('/your_url_path')
        response = serversfaults_view(request)

        # Check that the response has a status code of 200 (HTTP OK)
        self.assertEqual(response.status_code, 200)

        # Check that the response contains the plot data
        self.assertContains(response, 'mocked_plot_data')
