import element_controller
import machine_controller
from cwmath.cwvector3d import CwVector3d

from essentials.adapters._utils import to_cadwork_vector
from essentials.models import ElementId


class ElementControllerWrapper:

    @staticmethod
    def create_rectangular_beam(
            width: float,
            height: float,
            length: float,
            start: CwVector3d,
            end: CwVector3d,
            height_vec: CwVector3d
    ) -> ElementId:
        return element_controller.create_rectangular_beam_vectors(
            width,
            height,
            length,
            to_cadwork_vector(start),
            to_cadwork_vector(end),
            to_cadwork_vector(height_vec)
        )

    @staticmethod
    def create_circular_beam(
            diameter: float,
            length: float,
            start: CwVector3d,
            end: CwVector3d,
            height_vec: CwVector3d
    ) -> ElementId:
        return element_controller.create_circular_beam_vectors(
            diameter,
            length,
            to_cadwork_vector(start),
            to_cadwork_vector(end),
            to_cadwork_vector(height_vec)
        )
