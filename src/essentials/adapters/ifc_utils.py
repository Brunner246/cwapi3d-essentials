from dataclasses import dataclass
from enum import verify, EnumCheck, Enum, auto


@verify(EnumCheck.UNIQUE)
class IfcSchema(Enum):
    IFC2X3 = auto(), 0
    IFC4 = auto()


@verify(EnumCheck.UNIQUE)
class ExportMode(Enum):
    SILENT = auto(), 0
    VERBOSE = auto()


@dataclass(frozen=True, slots=True, kw_only=True)
class ExportOptions:
    schema: IfcSchema
    mode: ExportMode
    with_settings: bool = False
