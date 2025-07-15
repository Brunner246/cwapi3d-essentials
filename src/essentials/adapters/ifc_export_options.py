from cadwork import (ifc_options, ifc_options_aggregation, ifc_options_project_data)


class IfcExportOptions:
    def __init__(self):
        from .ifc_property_options import IfcPropertyOptions
        from .ifc_level_of_detail_options import IfcLevelOfDetailOptions

        self.options: ifc_options = ifc_options()
        self.property_options = IfcPropertyOptions(self.options.get_ifc_options_properties())
        self.level_of_detail = IfcLevelOfDetailOptions(self.options.get_ifc_options_level_of_detail())

    @property
    def aggregation(self) -> ifc_options_aggregation:
        return self.options.get_ifc_options_aggregation()

    @property
    def project_data(self) -> ifc_options_project_data:
        return self.options.get_ifc_options_project_data()
