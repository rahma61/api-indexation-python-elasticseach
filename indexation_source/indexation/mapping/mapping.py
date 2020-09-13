"""
  This is the module mapping
  """
"""Ici un appel à la méthode de correction des dates"""
from indexation_source.indexation.mapping.mapping_controle import corrige_date_oeie_avis


class Mapping:
    """
      This is the class Mapping
      """
    def avis_mapping(self, resource):
        """
          This method makes the mapping af the ressource
          """
        data = {
            "id": resource.get("avis_numero_avis", '').encode('iso-8859-15').decode('utf-8') +
                  "_" + resource.get('avis_code_base', '').encode('iso-8859-15').decode('utf-8'),
            "ref": resource.get("avis_numero_avis", '').encode('iso-8859-15').decode('utf-8'),
            "baseCode": resource.get('avis_code_base', '').encode('iso-8859-15').decode('utf-8'),
            "baseCode42C": resource.get('CPT_42C', '').encode('iso-8859-15').decode('utf-8'),
            "baseCodeGDP":
                resource.get('avis_compte_prometee', '').encode('iso-8859-15').decode('utf-8'),
            "DRCode": resource.get('avis_oeie_code_dr', '').encode('iso-8859-15').decode('utf-8'),
            "sectorCode": resource.get('avis_code_secteur', '').encode('iso-8859-15').decode(
                'utf-8'),
            "subReasonCode":
                resource.get('avis_code_sous_justif', '').encode('iso-8859-15').decode('utf-8'),
            "subReasonLabel":
                resource.get('avis_libelle_ssjustif', '').encode('iso-8859-15').decode('utf-8'),
            "priorityCode":
                resource.get('avis_code_priorite', '').encode('iso-8859-15').decode('utf-8'),
            "customerExpectedDate":
                corrige_date_oeie_avis(resource.get('avis_date_souhait_client', '')),
            "studyExpectedDate":
                corrige_date_oeie_avis(resource.get(
                    'avis_date_souhaitee_retour_etude', '')),
            "hasRelatedOEIE":
                resource.get('avis_indicateur_oeie', '').encode('iso-8859-15').decode('utf-8'),
            "hasPilotageResponse":
                resource.get('avis_indicateur_reponse', '').encode('iso-8859-15').decode('utf-8'),
            'resourceBusinessName': 'as',

            'adress': {
                "cityCode": resource.get('avis_code_commune', '').encode('iso-8859-15').decode(
                    'utf-8'),
                "cityName": resource.get('avis_lib_commune', '').encode('iso-8859-15').decode(
                    'utf-8'),
                "provinceCode":
                    resource.get('avis_code_departement', '').encode('iso-8859-15').decode(
                        'utf-8'),
                "streetName":
                    resource.get('avis_lib_voie', '').encode('iso-8859-15').decode('utf-8'),
                "streetNumber":
                    resource.get('avis_no_voie', '').encode('iso-8859-15').decode('utf-8'),
            },
            'localLoop': {
                "connectionCenterCode":
                    resource.get('avis_code_centre', '').encode('iso-8859-15').decode('utf-8'),
                "connectionZoneCode":
                    resource.get('avis_code_zone', '').encode('iso-8859-15').decode('utf-8'),
                "equipmentObservation":
                    resource.get('avis_equipement', '').encode('iso-8859-15').decode('utf-8'),
            },
            'response': {
                "firstResponseCode":
                    resource.get('avis_rep1_avis', '').encode('iso-8859-15').decode('utf-8'),
                "firstResponseLabel":
                    resource.get('avis_lrepas1', '').encode('iso-8859-15').decode('utf-8'),
                "secondResponseCode":
                    resource.get('avis_rep2_avis', '').encode('iso-8859-15').decode('utf-8'),
                "secondResponseLabel":
                    resource.get('avis_lrepas2', '').encode('iso-8859-15').decode('utf-8'),
                "responseNote":
                    resource.get('avis_comrep', '').encode('iso-8859-15').decode('utf-8'),
                "responseUserID":
                    resource.get('avis_repondeur', '').encode('iso-8859-15').decode('utf-8'),
            },
            'creation': {
                "creationUserId":
                    resource.get('avis_createur_avis', '').encode('iso-8859-15').decode('utf-8'),
                "creatorDepartmentCode":
                    resource.get('avis_service', '').encode('iso-8859-15').decode('utf-8'),
                "creationDate":
                    corrige_date_oeie_avis(resource.get('avis_date_creation', '')),
                "creationNote":
                    resource.get(
                        'avis_commentaire_creation', '').encode('iso-8859-15').decode('utf-8'),
            },
            'cancellation': {
                "cancellationUserID":
                    resource.get('avis_agent_annulation', '').encode('iso-8859-15').decode(
                        'utf-8'),
                "cancellationDate":
                    corrige_date_oeie_avis(resource.get('avis_date_annulation', '')),
                "cancellationNote":
                    resource.get(
                        'avis_commentaire_annulation', '').encode('iso-8859-15').decode('utf-8'),
            },
            'relatedCopperRessourceOrder': {
                "ref": resource.get(
                    'avis_numero_demande', '').encode('iso-8859-15').decode('utf-8'),
                "holderName":
                    resource.get('avis_titulaire_demande', '').encode('iso-8859-15').decode(
                        'utf-8'),
                "designationNumber":
                    resource.get('avis_nd', '').encode('iso-8859-15').decode('utf-8'),
            },
            'relatedOEIE': {
                "id": resource.get('oeie_numero_oeie', '').encode('iso-8859-15').decode('utf-8'),
                "state": resource.get('oeie_code_etat', '').encode('iso-8859-15').decode('utf-8'),
                "stateLabel":
                    resource.get('oeie_libelle_etat', '').encode('iso-8859-15').decode('utf-8'),
                "operationType":
                    resource.get(
                        'oeie_code_type_operation',
                        '').encode('iso-8859-15').decode('utf-8'),
                "baseGDP":
                    resource.get(
                        'oeie_code_prometee', '').encode('iso-8859-15').decode('utf-8'),
                "sectorCode":
                    resource.get(
                        'oeie_code_secteur', '').encode('iso-8859-15').decode('utf-8'),
                "connectionCenterCode":
                    resource.get(
                        'oeie_code_centre', '').encode('iso-8859-15').decode('utf-8'),
                "connectionZoneCode":
                    resource.get(
                        'oeie_code_zone', '').encode('iso-8859-15').decode('utf-8'),
                "creationUserId":
                    resource.get(
                        'oeie_charge_affaire', '').encode('iso-8859-15').decode('utf-8'),
                "creationDate":
                    corrige_date_oeie_avis(resource.get(
                        'oeie_date_creation', '')),
                "creationNotes":
                    resource.get(
                        'oeie_commentaire_creation', ''
                    ).encode('iso-8859-15').decode('utf-8'),
                "completionDeadline":
                    corrige_date_oeie_avis(resource.get(
                        'oeie_date_limite_rea', '')),
                "completionDate":
                    corrige_date_oeie_avis(resource.get(
                        'oeie_date_rea', '')),
                "GDPOperationCode":
                    resource.get(
                        'oeie_operation_gdp', ''
                    ).encode('iso-8859-15').decode('utf-8'),
                "copperRessourcesOrdersRef":
                    resource.get(
                        'oeie_numero_demande', ''
                    ).encode('iso-8859-15').decode('utf-8'),
                "RXXDate":
                    resource.get(
                        'oeie_date_rdv_demande', ''
                    ).encode('iso-8859-15').decode('utf-8'),
                "initialCompletionDeadline":
                    resource.get(
                        'oeie_dlri', ''
                    ).encode('iso-8859-15').decode('utf-8'),
                "outSourcedStudyCAFF":
                    resource.get(
                        'oeie_pibl_caffref', ''
                    ).encode('iso-8859-15').decode('utf-8'),
                "OEIEcode":
                    resource.get(
                        'oeie_code_oeie', ''
                    ).encode('iso-8859-15').decode('utf-8'),
                "operationReasonCode":
                    resource.get(
                        'opnot_code_justif', ''
                    ).encode('iso-8859-15').decode('utf-8'),
                "operationLabel":
                    resource.get(
                        'opnot_libelle_op', ''
                    ).encode('iso-8859-15').decode('utf-8'),

            }
        }
        return data
