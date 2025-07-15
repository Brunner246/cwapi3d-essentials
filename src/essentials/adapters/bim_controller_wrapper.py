from typing import Callable

from essentials.adapters.ifc_export_strategies import IfcExportStrategy, Ifc2x3VerboseExportStrategy, \
    Ifc2x3ExportStrategy, Ifc4ExportStrategy, Ifc2x3WithOptionsExportStrategy, Ifc4WithOptionsExportStrategy
from essentials.adapters.ifc_utils import ExportOptions, IfcSchema, ExportMode


class IfcExportFactory:
    @staticmethod
    def create_export_function(export_options: ExportOptions) -> Callable[[...], IfcExportStrategy]:
        match export_options:
            case ExportOptions(schema=IfcSchema.IFC2X3, mode=ExportMode.VERBOSE, with_settings=False):
                return lambda _: Ifc2x3VerboseExportStrategy()
            case ExportOptions(schema=IfcSchema.IFC2X3, mode=ExportMode.SILENT, with_settings=False):
                return lambda _: Ifc2x3ExportStrategy()
            case ExportOptions(schema=IfcSchema.IFC4, mode=ExportMode.SILENT, with_settings=False):
                return lambda _: Ifc4ExportStrategy()
            case ExportOptions(schema=IfcSchema.IFC2X3, mode=ExportMode.SILENT, with_settings=True):
                return lambda _settings: Ifc2x3WithOptionsExportStrategy(_settings)
            case ExportOptions(schema=IfcSchema.IFC4, mode=ExportMode.SILENT, with_settings=True):
                return lambda _settings: Ifc4WithOptionsExportStrategy(_settings)
            case _:
                raise ValueError(f"Unsupported export options: {export_options}")
