from elasticsearch import Elasticsearch


class ConnectionEs:
    def __init__(self, es):

        self.es = Elasticsearch(es)

    def perform_index(self, name, object_id, mapped_object):
        """On utilise la méthode index de Elasticsearch pour l'indexation et la réindexation"""
        return self.es.index(index=name, id=object_id, body=mapped_object)

    def perform_desindex(self, name, id):
        """On utilise la méthode delete de Elasticsearch pour la désindexation"""
        return self.es.delete(index=name, id=id)


