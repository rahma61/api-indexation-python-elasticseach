"""
This module tests controller
"""
import json
import unittest
from unittest.mock import patch
from starlette.testclient import TestClient
from indexation_source.indexation.controller.controller import Controller
from indexation_source.indexation.mapping.mapping import Mapping
from indexation_source.indexation.service.service import Service
from run import app
from indexation_source.tests.test_mapping import DATA as OBJECT_MAPPED, RESSOURCE

MAPPING = Mapping()
SERVICE = Service()
CONTROLLER = Controller()
LIST_OBJECT_TO_MAP = {
    "data": [
        RESSOURCE
    ]
}
LIST_OBJECT_TO_DESINDEX = {
    "data": [
        {"id": "20"}
    ]
}


class TestController(unittest.TestCase):
    """
     This class tests controller
     """

    @patch.object(Service, 'service_perform_index')
    @patch.object(Mapping, 'avis_mapping')
    @patch.object(Controller, 'result')
    @patch.object(Controller, 'status')
    def test_controller_perform_index(self, mock_status, mock_result, mock_avis_mapping,
                                      mock_service_perform_index):
        """
         This function tests index
         """
        mock_status.return_value = 201
        mock_result.return_value = (2, 0)
        mock_avis_mapping.return_value = OBJECT_MAPPED

        client = TestClient(app)
        mock_service_perform_index.return_value = (201, 'created', '7')
        response = client.post('/api/v1/avis/index', data=json.dumps(LIST_OBJECT_TO_MAP))
        self.assertEqual(response.status_code, 201)
        response = client.post('/api/v1/avis/index', data="a")
        self.assertEqual(response.status_code, 200)

    @patch.object(Service, 'service_perform_reindex')
    @patch.object(Mapping, 'avis_mapping')
    @patch.object(Controller, 'result')
    @patch.object(Controller, 'status')
    def test_controller_perform_reindex(self, mock_status, mock_result, mock_avis_mapping,
                                        mock_service_perform_reindex):

        mock_status.return_value = 201
        mock_result.return_value = (2, 0)
        mock_avis_mapping.return_value = OBJECT_MAPPED

        client = TestClient(app)
        mock_service_perform_reindex.return_value = (201, 'created', '7')
        response = client.post('/api/v1/avis/reindex', data=json.dumps(LIST_OBJECT_TO_MAP))
        self.assertEqual(response.status_code, 201)
        response = client.post('/api/v1/avis/reindex', data="a")
        self.assertEqual(response.status_code, 200)

    @patch.object(Controller, 'result')
    @patch.object(Controller, 'status')
    @patch.object(Service, 'service_perform_desindex')
    def test_controller_perform_desindex(self, mock_service_perform_desindex, mock_status, mock_result, ):

        mock_status.return_value = 200
        mock_result.return_value = (2, 0)

        client = TestClient(app)
        mock_service_perform_desindex.return_value = (200, 'deleted', '7')
        response = client.post('/api/v1/avis/desindex', data=json.dumps(LIST_OBJECT_TO_DESINDEX))
        self.assertEqual(response.status_code, 200)
        response = client.post('/api/v1/avis/desindex', data="a")
        self.assertEqual(response.status_code, 200)


def test_status():

    assert CONTROLLER.status([400, 400]) == 400
    assert CONTROLLER.status([201, 201]) == 201
    assert CONTROLLER.status([200, 200]) == 200
    assert CONTROLLER.status([200, 201]) == 200
    assert CONTROLLER.status([400, 200]) == 206


def test_result():

    assert CONTROLLER.result([200, 201]) == (2, 0)
    assert CONTROLLER.result([400, 201]) == (1, 1)


if __name__ == '__main__':
    unittest.main()
