"""
This is the module service
"""
from indexation_source.common.connection.connection import ConnectionEs


class Service:
    """
    This is the class service
    """
    def __init__(self):
        self.con = ConnectionEs(es="http://localhost:9200/")

    def service_perform_index(self, object_mapped):

        try:
            res = self.con.perform_index(name="avis", object_id=object_mapped['id'],
                                         mapped_object=object_mapped)
            print("res", res)
            if res['result'] == 'updated':
                return 200, res['result'], object_mapped['id']
            elif res['result'] == 'created':
                return 201, res['result'], object_mapped['id']
        except:
            return 400, "Bad request"

    def service_perform_desindex(self, id_obj):
        """
          This is the method desindex
          """
        try:
            res = self.con.perform_desindex(name="avis", id=id_obj)
            print("res", res)

            if res['result'] == 'deleted':
                return 200, res['result'], id_obj
        except:
            return 400, "Object not found"

    def service_perform_reindex(self, object_mapped):

        try:
            res = self.con.perform_index(name="avis_next", object_id=object_mapped['id'],
                                         mapped_object=object_mapped)
            print("res", res)
            if res['result'] == 'updated':
                return 200, res['result'], object_mapped['id']
            elif res['result'] == 'created':
                return 201, res['result'], object_mapped['id']
        except:
            return 400, "Bad request"
