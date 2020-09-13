"""
This is the module controller
"""
import time
from starlette.responses import JSONResponse, Response
from indexation_source.indexation.mapping.mapping import Mapping
from indexation_source.indexation.service.service import Service

SERVICE = Service()
MAPPING = Mapping()


class Controller:
    """
    This is the class controller
    """
    async def controller_perform_index(self, request):
        """
        This is the method controller_index
        """
        try:
            start_time = time.time()
            list_object_to_map = await request.json()
            list_object_mapped = []
            for object_to_map in list_object_to_map["data"]:
                object_mapped = MAPPING.avis_mapping(object_to_map)
                print("object_mapped", object_mapped)
                list_object_mapped.append(object_mapped)
            status_codes = []
            for object_mapped in list_object_mapped:
                index_result = SERVICE.service_perform_index(object_mapped)
                print("index_result", index_result)
                status_codes.append(index_result[0])
            print("status codes", status_codes)
            global_rtt = time.time() - start_time
            result = Controller.result(self, status_codes)
            result = {'OK': result[0], 'NOK': result[1], "rtt": global_rtt}
            st_code = Controller.status(self, status_codes)
            return JSONResponse(result, status_code=st_code, media_type='application/json')
        except:
            return Response("Bad request")

    async def controller_perform_desindex(self, request):
        """
        This is the method controller_desindex
        """
        start_time = time.time()
        try:
            data = await request.json()
            print("data", data)
            list_id_to_dexindex = []
            for object_id in data["data"]:
                id_obj = object_id.get("id")
                list_id_to_dexindex.append(id_obj)
            print("list_id_to_dexindex", list_id_to_dexindex)
            status_codes = []
            for id_obj in list_id_to_dexindex:
                desindex_result = SERVICE.service_perform_desindex(id_obj)
                print("desindex_result", desindex_result)
                status_codes.append(desindex_result[0])
            global_rtt = int(1000 * (time.time() - start_time))
            result = Controller.result(self, status_codes)
            result = {'OK': result[0], 'NOK': result[1], "rtt": global_rtt}
            st_code = Controller.status(self, status_codes)
            return JSONResponse(result, status_code=st_code, media_type='application/json')

        except:
            return Response("Bad request")

    async def controller_perform_reindex(self, request):
        """
        This is the method controller_desindex
        """
        try:
            start_time = time.time()
            list_object_to_map = await request.json()
            list_object_mapped = []
            for object_to_map in list_object_to_map["data"]:
                object_mapped = MAPPING.avis_mapping(object_to_map)
                print("object_mapped", object_mapped)
                list_object_mapped.append(object_mapped)
            status_codes = []
            for object_mapped in list_object_mapped:
                reindex_result = SERVICE.service_perform_reindex(object_mapped)
                print("index_result", reindex_result)
                status_codes.append(reindex_result[0])
            print("status codes", status_codes)
            global_rtt = time.time() - start_time
            result = Controller.result(self, status_codes)
            result = {'OK': result[0], 'NOK': result[1], "rtt": global_rtt}
            st_code = Controller.status(self, status_codes)
            return JSONResponse(result, status_code=st_code, media_type='application/json')

        except:
            return Response("Bad request")

    def result(self, status_codes):
        """
        This function returns the number of OK and NOK
        """
        res_ok = 0
        res_nok = 0
        for status_code in status_codes:
            if status_code in [200, 201]:
                res_ok = res_ok + 1
            elif status_code == 400:
                res_nok = res_nok + 1
        return res_ok, res_nok

    def status(self, status_codes):
        """
        This function calculates the status code
        """
        global STATE_CODE
        if all(x == status_codes[0] for x in status_codes):
            if status_codes[0] == 400:
                STATE_CODE = 400
            elif status_codes[0] == 201:
                STATE_CODE = 201
            elif status_codes[0] == 200:
                STATE_CODE = 200
        elif 400 in status_codes:
            STATE_CODE = 206
        elif 200 in status_codes:
            STATE_CODE = 200
        return STATE_CODE
