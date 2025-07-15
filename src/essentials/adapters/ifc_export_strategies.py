from abc import ABC, abstractmethod
from typing import List, Callable

from essentials.adapters import IfcExportOptions
from essentials.adapters.ifc_utils import ExportOptions, ExportMode, IfcSchema
from essentials.models import ElementId


class IfcExportStrategy(ABC):
    @abstractmethod
    def export(self, elements: List[ElementId], file_path: str) -> bool:
        raise NotImplementedError("Export method must be implemented by subclasses.")


class Ifc4WithOptionsExportStrategy(IfcExportStrategy):
    def __init__(self, options: IfcExportOptions):
        self.options = options

    def export(self, elements: List[ElementId], file_path: str) -> bool:
        import bim_controller as bc
        return bc.export_ifc4_silently_with_options(elements, file_path, self.options.options)


class Ifc2x3WithOptionsExportStrategy(IfcExportStrategy):
    def __init__(self, options: IfcExportOptions):
        self.options = options

    def export(self, elements: List[ElementId], file_path: str) -> bool:
        import bim_controller as bc
        return bc.export_ifc2x3_silently_with_options(elements, file_path, self.options.options)


class Ifc2x3ExportStrategy(IfcExportStrategy):
    def export(self, elements: List[ElementId], file_path: str) -> bool:
        import bim_controller as bc
        return bc.export_ifc2x3_silently(elements, file_path)


class Ifc4ExportStrategy(IfcExportStrategy):
    def export(self, elements: List[ElementId], file_path: str) -> bool:
        import bim_controller as bc
        return bc.export_ifc4_silently(elements, file_path)


class Ifc2x3VerboseExportStrategy(IfcExportStrategy):
    def export(self, elements: List[ElementId], file_path: str) -> bool:
        import bim_controller as bc
        return bc.export_ifc(elements, file_path)



