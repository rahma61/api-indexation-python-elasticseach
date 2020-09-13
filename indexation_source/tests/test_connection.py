"""
This module tests connection
"""
import unittest
from unittest.mock import patch
from elasticsearch import Elasticsearch
from indexation_source.common.connection.connection import ConnectionEs
from indexation_source.tests.test_service import MAPPED_OBJECT


CONNECTIONES = ConnectionEs("http://localhost:9200/")


class MyTestCase(unittest.TestCase):
    """
    This class tests connection
    """
    @patch.object(Elasticsearch, 'index')
    def test_service_perform_index(self, mock_index):

        index = CONNECTIONES.perform_index("avis", 55, MAPPED_OBJECT)
        mock_index.assert_called_with(index="avis", id=55, body=MAPPED_OBJECT)

    @patch.object(Elasticsearch, 'delete')
    def test_service_perform_desindex(self, mock_delete):

        delete = CONNECTIONES.perform_desindex("avis", 55)
        mock_delete.assert_called_with(index="avis", id=55)


if __name__ == '__main__':
    unittest.main()
