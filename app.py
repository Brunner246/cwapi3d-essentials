import os
import sys
from pathlib import Path

import logging

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

from cwmath.cwvector3d import CwVector3d
from essentials.beam_elements.beam_factory import RectangularBeamFactory, CircularBeamFactory, create_beam
from essentials.models import Dimensions, AxisSystem

if __name__ == '__main__':
    rectangular_factory = RectangularBeamFactory()
    circular_factory = CircularBeamFactory()

    dimensions: Dimensions = Dimensions(length=1_000.0, width=120.0, height=240.0)
    axis_system: AxisSystem = AxisSystem(
        start=CwVector3d(0, 0, 0),
        end=CwVector3d(1_000, 0, 0),
        height=CwVector3d(0, 0, 1)
    )

    beam_id = create_beam(dimensions, axis_system, circular_factory)
