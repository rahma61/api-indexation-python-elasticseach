import uvicorn
from starlette.applications import Starlette
from indexation_source.indexation.controller.controller import Controller

CONTROLLER = Controller()
app = Starlette()
"""on utilise le framework Starlette"""


class Run:
    app.add_route("/api/v1/avis/index", CONTROLLER.controller_perform_index, methods=["POST"])
    app.add_route("/api/v1/avis/desindex", CONTROLLER.controller_perform_desindex, methods=["POST"])
    app.add_route("/api/v1/avis_next/reindex", CONTROLLER.controller_perform_reindex, methods=["POST"])


if __name__ == '__main__':
    """Connection to server Uvicorn on port 8000"""
    uvicorn.run(app, host="localhost", port=8000, debug=True)
