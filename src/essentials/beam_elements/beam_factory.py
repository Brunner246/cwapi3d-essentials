from typing import Protocol

from essentials.adapters import ElementControllerWrapper
from essentials.models import AxisSystem, ElementId
from essentials.models import Dimensions


class BeamFactory(Protocol):
    def create(self, dimensions: Dimensions, axis_system: AxisSystem) -> ElementId:
        ...


class RectangularBeamFactory:
    @staticmethod
    def create(dimensions: Dimensions, axis_system: AxisSystem) -> ElementId:
        return ElementControllerWrapper.create_rectangular_beam(
            dimensions.width,
            dimensions.height,
            dimensions.length,
            axis_system.p1,
            axis_system.p2,
            axis_system.p3
        )


class CircularBeamFactory:
    @staticmethod
    def create(dimensions: Dimensions, axis_system: AxisSystem) -> ElementId:
        return ElementControllerWrapper.create_circular_beam(
            dimensions.width,  # treating width as diameter
            dimensions.length,
            axis_system.p1,
            axis_system.p2,
            axis_system.p3
        )


def create_beam(dimensions: Dimensions, axis_system: AxisSystem, factory: BeamFactory) -> ElementId:
    return factory.create(dimensions, axis_system)
