import logging
import os
import sys
from pathlib import Path
from typing import Callable


import cadwork
import element_controller as ec
import geometry_controller as gc

facets = gc.get_element_facets()
facets.get_external_polygon_for_reference_face()


visible_elements = ec.get_visible_identifiable_element_ids()
if not visible_elements:
    raise ValueError("No visible identifiable elements found.")

element_facets: cadwork.facet_list = ec.get_facets_with_lasso(visible_elements)
if not element_facets:
    raise ValueError("No facets found in the selected elements.")

vertex_list: cadwork.vertex_list = element_facets.at(0)

if not vertex_list:
    raise ValueError("No vertices found in the selected facets.")

ec.create_surface(vertex_list)

for idx, vertice in enumerate(vertex_list): # type: ignore[assignment]
    line_begin_vertex = vertice
    line_end_vertex = vertex_list[(idx + 1) % len(vertex_list)] # type: ignore[assignment]

    ec.create_line_points(line_begin_vertex, line_end_vertex)

# for i in range(element_facets.count()):
#     face = element_facets.at(i)
#     if face.count() > 2:
#         lPnts=[]
#         for j in range(face.count()):
#             if face.at(j) not in lPnts:
#                 lPnts.append(face.at(j))
#         print(lPnts)
#         for j in range(len(lPnts)-1):
#             toto=ec.create_line_points(lPnts[j],lPnts[j+1])
#         surface=ec.create_surface(lPnts)
#         print(surface)
#         list_elements.append(surface)

import geometry_controller as gc

# facets = gc.get_element_facets()
# polygon = facets.get_external_polygon_for_reference_face()
# for i, p in enumerate(polygon):
#     print(f"Point {i}: {p.x}, {p.y}, {p.z}")

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(f"{__name__}.app")

poetry_cache_dir = Path(os.environ["LOCALAPPDATA"]) / "pypoetry" / "Cache" / "virtualenvs"
venv_name = "cwapi3d-essentials-RSoPvMlx-py3.12"
poetry_venv_path = poetry_cache_dir / venv_name / "Lib" / "site-packages"
os.environ["POETRY_VENV"] = str(poetry_venv_path)

logger.debug(f"Poetry venv path: {poetry_venv_path}")
# os.getenv("POETRY_VENV", "Not set")
if poetry_venv_path.exists():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    src_dir = Path(base_dir) / "src"
    site_packages_path = os.environ["POETRY_VENV"]
    paths = [
        site_packages_path,
        base_dir,
        str(src_dir),
    ]
    sys.path.extend(paths)
    os.environ['PYTHONPATH'] = os.pathsep.join([*paths, os.environ.get('PYTHONPATH', '')])
    logger.debug(f"Python paths updated: {paths}")

else:
    print(f"Warning: Poetry venv path not found: {poetry_venv_path}")
    sys.exit(1)

from essentials.adapters import IfcExportOptions
from essentials.adapters.bim_controller_wrapper import ExportOptions, IfcSchema, ExportMode, IfcExportFactory, \
    IfcExportStrategy
from essentials.adapters.element_controller_wrapper import get_active_elements

if __name__ == '__main__':
    ifc_options = IfcExportOptions()
    ifc_options.property_options.export_bim_wood_property = True
    ifc_options.property_options.ignore_user_attributes_used_in_user_psets = True
    ifc_options.property_options.export_cadwork_3d_pset = True
    ifc_options.property_options.export_quantity_sets = True

    ifc_options.level_of_detail.export_installation_rectangular_materialization = True
    ifc_options.level_of_detail.export_installation_round_materialization = True
    ifc_options.level_of_detail.export_end_type_materialization = True
    ifc_options.level_of_detail.export_vba_drilling = True
    ifc_options.level_of_detail.cut_end_type_counterparts = True
    ifc_options.level_of_detail.cut_drilling = True

    options = ExportOptions(schema=IfcSchema.IFC4, mode=ExportMode.SILENT, with_settings=True)
    ifc_export_strategy: Callable[[None | IfcExportOptions], IfcExportStrategy] = IfcExportFactory.create_export_function(
        options)

    export_obj = ifc_export_strategy(ifc_options)
    export_obj.export(get_active_elements(), str(Path.home() / "Downloads" / "test.ifc"))

























    # ifc_export_func(get_active_elements(),
    #                 str(Path.home() / "Downloads" / "test.ifc"),
    #                 ifc_options.options)

    # rectangular_factory = RectangularBeamFactory()
    # circular_factory = CircularBeamFactory()
    #
    # dimensions: Dimensions = Dimensions(length=1_000.0, width=120.0, height=240.0)
    # axis_system: AxisSystem = AxisSystem(
    #     start=CwVector3d(0, 0, 0),
    #     end=CwVector3d(1_000, 0, 0),
    #     height=CwVector3d(0, 0, 1)
    # )
    #
    # beam_id = create_beam(dimensions, axis_system, circular_factory)
