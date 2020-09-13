"""
This module tests test_mapping
"""
import unittest
from indexation_source.indexation.mapping.mapping import Mapping

MAPPING = Mapping()
DATA = {
    "id":"122_1",
    "ref": "122",
    "baseCode": "1",
    "baseCode42C": "12",
    "baseCodeGDP": "a",
    "DRCode": "b",
    "sectorCode": "m",
    "subReasonCode": "3R4",
    "subReasonLabel": "c",
    "priorityCode": "5Rf",
    "customerExpectedDate": "12-01-2016",
    "studyExpectedDate": "12-3-2016",
    "hasRelatedOEIE": "d",
    "hasPilotageResponse": "e",
    "resourceBusinessName": "as",
    "adress": {
        "cityCode": "1",
        "cityName": "2",
        "provinceCode": "2A",
        "streetName": "aa",
        "streetNumber": "3"
    },
    "localLoop": {
        "connectionCenterCode": "a",
        "connectionZoneCode": "a",
        "equipmentObservation": "v"
    },
    "response": {
        "firstResponseCode": "aa",
        "firstResponseLabel": "bb",
        "secondResponseCode": "b1",
        "secondResponseLabel": "na",
        "responseNote": "dd",
        "responseUserID": "h"
    },
    "creation": {
        "creationUserId": "d4",
        "creatorDepartmentCode": "k3",
        "creationDate": "AED",
        "creationNote": "9i"
    },
    "cancellation": {
        "cancellationUserID": "j8",
        "cancellationDate": "d4",
        "cancellationNote": "l9"
    },
    "relatedCopperRessourceOrder": {
        "ref": "m8",
        "holderName": "r",
        "designationNumber": "88"
    },
    "relatedOEIE": {
        "id": "a",
        "state": "b",
        "stateLabel": "c",
        "operationType": "d",
        "baseGDP": "t",
        "sectorCode": "k",
        "connectionCenterCode": "a",
        "connectionZoneCode": "p",
        "creationUserId": "b",
        "creationDate": "r",
        "creationNotes": "e",
        "completionDeadline": "o",
        "completionDate": "m",
        "GDPOperationCode": "",
        "copperRessourcesOrdersRef": "",
        "RXXDate": "",
        "initialCompletionDeadline": "",
        "outSourcedStudyCAFF": "",
        "OEIEcode": "",
        "operationReasonCode": "",
        "operationLabel": ""
    }
}
RESSOURCE = {
    "avis_numero_avis": "122",
    "avis_code_base": "1",
    "CPT_42C": "12",
    "avis_compte_prometee": "a",
    "avis_oeie_code_dr": "b",
    "avis_code_secteur": "m",
    "avis_code_sous_justif": "3R4",
    "avis_libelle_ssjustif": "c",
    "avis_code_priorite": "5Rf",
    "avis_date_souhait_client": "12/01/2016",
    "avis_date_souhaitee_retour_etude": "12/3/2016",
    "avis_indicateur_oeie": "d",
    "avis_indicateur_reponse": "e",
    "avis_code_commune": "1",
    "avis_lib_commune": "2",
    "avis_code_departement": "2A",
    "avis_lib_voie": "aa",
    "avis_no_voie": "3",
    "avis_code_centre": "a",
    "avis_code_zone": "a",
    "avis_equipement": "v",
    "avis_rep1_avis": "aa",
    "avis_lrepas1": "bb",
    "avis_rep2_avis": "b1",
    "avis_lrepas2": "na",
    "avis_comrep": "dd",
    "avis_repondeur": "h",
    "avis_createur_avis": "d4",
    "avis_service": "k3",
    "avis_date_creation": "AED",
    "avis_commentaire_creation": "9i",
    "avis_agent_annulation": "j8",
    "avis_date_annulation": "d4",
    "avis_commentaire_annulation": "l9",
    "avis_numero_demande": "m8",
    "avis_titulaire_demande": "r",
    "avis_nd": "88",
    "oeie_numero_oeie": "a",
    "oeie_code_etat": "b",
    "oeie_libelle_etat": "c",
    "oeie_code_type_operation": "d",
    "oeie_code_prometee": "t",
    "oeie_code_secteur": "k",
    "oeie_code_centre": "a",
    "oeie_code_zone": "p",
    "oeie_charge_affaire": "b",
    "oeie_date_creation": "r",
    "oeie_commentaire_creation": "e",
    "oeie_date_limite_rea": "o",
    "oeie_date_rea": "m",
    "oeie_operation_gdp": "",
    "oeie_numero_demande": "",
    "oeie_date_rdv_demande": "",
    "oeie_dlri": "",
    "oeie_pibl_caffref": "",
    "oeie_code_oeie": "",
    "opnot_code_justif": "",
    "opnot_libelle_op": ""
}


class TestMapping(unittest.TestCase):
    """
     This class tests connection
     """
    def test_avis_mapping(self):

        assert MAPPING.avis_mapping(RESSOURCE) == DATA


if __name__ == '__main__':
    unittest.main()
