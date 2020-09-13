"""
This module tests service
"""
import unittest
from unittest.mock import patch
from indexation_source.common.connection.connection import ConnectionEs
from indexation_source.indexation.service.service import Service

SERVICE = Service()
MAPPED_OBJECT = {
    "id": "122_1",
    "ref": "122",
    "baseCode": "15",
    "baseCode42C": "152",
    "baseCodeGDP": "a7",
    "DRCode": "b9",
    "sectorCode": "m6",
    "subReasonCode": "3R47",
    "subReasonLabel": "2c",
    "priorityCode": "53Rf",
    "customerExpectedDate": "12-01-2016",
    "studyExpectedDate": "12-3-2016",
    "hasRelatedOEIE": "d6",
    "hasPilotageResponse": "3e",
    "resourceBusinessName": "4as",
    "adress": {
        "cityCode": "51",
        "cityName": "62",
        "provinceCode": "32A",
        "streetName": "a4a",
        "streetNumber": "37"
    },
    "localLoop": {
        "connectionCenterCode": "8a",
        "connectionZoneCode": "6a",
        "equipmentObservation": "7v"
    },
    "response": {
        "firstResponseCode": "3aa",
        "firstResponseLabel": "",
        "secondResponseCode": "",
        "secondResponseLabel": "",
        "responseNote": "",
        "responseUserID": ""
    },
    "creation": {
        "creationUserId": "",
        "creatorDepartmentCode": "",
        "creationDate": "AED",
        "creationNote": ""
    },
    "cancellation": {
        "cancellationUserID": "",
        "cancellationDate": "",
        "cancellationNote": ""
    },
    "relatedCopperRessourceOrder": {
        "ref": "m8",
        "holderName": "r",
        "designationNumber": ""
    },
    "relatedOEIE": {
        "id": "5",
        "state": "9",
        "stateLabel": "a",
        "operationType": "g",
        "baseGDP": "y",
        "sectorCode": "8",
        "connectionCenterCode": "y",
        "connectionZoneCode": "u",
        "creationUserId": "a",
        "creationDate": "l",
        "creationNotes": "2",
        "completionDeadline": "p",
        "completionDate": "p",
        "GDPOperationCode": "1",
        "copperRessourcesOrdersRef": "3",
        "RXXDate": "",
        "initialCompletionDeadline": "7",
        "outSourcedStudyCAFF": "8",
        "OEIEcode": "7",
        "operationReasonCode": "9",
        "operationLabel": "3"
    }
}
INDEX_UPDATE = {'_index': 'avis',
                '_type': '_doc',
                '_id': '55',
                '_version': 25,
                'result': 'updated',
                '_shards': {'total': 2,
                            'successful': 1,
                            'failed': 0
                            },
                '_seq_no': 1129, '_primary_term': 3}
INDEX_CREATE = {'_index': 'avis',
                '_type': '_doc',
                '_id': '55',
                '_version': 25,
                'result': 'created',
                '_shards': {'total': 2,
                            'successful': 1,
                            'failed': 0
                            },
                '_seq_no': 1129, '_primary_term': 3}
INDEX_DELETE = {'_index': 'avis',
                '_type': '_doc',
                '_id': '20',
                '_version': 3,
                'result': 'deleted',
                '_shards': {'total': 2,
                            'successful': 1,
                            'failed': 0},
                '_seq_no': 1191,
                '_primary_term': 3}
INDEX_NOT_FOUND = {'_index': 'avis',
                   '_type': '_doc',
                   '_id': '20',
                   '_version': 3,
                   'result': 'Object not found',
                   '_shards': {'total': 2,
                               'successful': 1,
                               'failed': 0},
                   '_seq_no': 1191,
                   '_primary_term': 3}


class TestService(unittest.TestCase):
    """
     This class tests service
     """
    @patch.object(ConnectionEs, 'perform_index')
    def test_service_perform_index(self, mock_perform_index):

        mock_perform_index.return_value = INDEX_UPDATE
        index_result = SERVICE.service_perform_index(MAPPED_OBJECT)
        self.assertEqual(index_result[0], 200)
        self.assertEqual(index_result[1], "updated")
        self.assertEqual(index_result[2], "122_1")
        index_result = SERVICE.service_perform_index({})
        self.assertEqual(index_result[0], 400)

        mock_perform_index.return_value = INDEX_CREATE
        index_result = SERVICE.service_perform_index(MAPPED_OBJECT)
        self.assertEqual(index_result[0], 201)
        self.assertEqual(index_result[1], "created")
        self.assertEqual(index_result[2], "122_1")

        mock_perform_index.assert_called_with(name='avis',
                                              object_id='122_1',
                                              mapped_object=MAPPED_OBJECT)

    @patch.object(ConnectionEs, 'perform_desindex')
    def test_service_perform_desindex_ok(self, mock_perform_desindex):

        mock_perform_desindex.return_value = INDEX_DELETE
        desindex_result = SERVICE.service_perform_desindex(20)
        self.assertEqual(desindex_result[1], "deleted")
        self.assertEqual(desindex_result[0], 200)
        mock_perform_desindex.assert_called_with(id=20, name='avis')

    def test_service_perform_desindex_not_ok(self):

        assert SERVICE.service_perform_desindex(20)[0] == 400

    @patch.object(ConnectionEs, 'perform_index')
    def test_service_perform_reindex(self, mock_perform_index):

        mock_perform_index.return_value = INDEX_UPDATE
        reindex_result = SERVICE.service_perform_reindex(MAPPED_OBJECT)
        self.assertEqual(reindex_result[0], 200)
        self.assertEqual(reindex_result[1], "updated")
        self.assertEqual(reindex_result[2], "122_1")

        mock_perform_index.return_value = INDEX_CREATE
        reindex_result = SERVICE.service_perform_reindex(MAPPED_OBJECT)
        self.assertEqual(reindex_result[0], 201)
        self.assertEqual(reindex_result[1], "created")
        self.assertEqual(reindex_result[2], "122_1")
        reindex_result = SERVICE.service_perform_reindex({})
        self.assertEqual(reindex_result[0], 400)

        mock_perform_index.assert_called_with(name='avis_next',
                                              object_id='122_1',
                                              mapped_object=MAPPED_OBJECT)


if __name__ == '__main__':
    unittest.main()
