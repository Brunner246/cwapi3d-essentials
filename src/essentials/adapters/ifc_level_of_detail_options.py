from cadwork import ifc_options_level_of_detail

class IfcLevelOfDetailOptions:
    def __init__(self, parent: ifc_options_level_of_detail):
        self.parent = parent
        self._level_of_detail: ifc_options_level_of_detail = parent

    @property
    def export_vba_drilling(self) -> bool:
        return self._level_of_detail.get_export_vba_drillings()

    @export_vba_drilling.setter
    def export_vba_drilling(self, value: bool) -> None:
        self._level_of_detail.set_export_vba_drillings(value)

    @property
    def cut_end_type_counterparts(self) -> bool:
        return self._level_of_detail.get_cut_endtype_counterparts()

    @cut_end_type_counterparts.setter
    def cut_end_type_counterparts(self, value: bool) -> None:
        self._level_of_detail.set_cut_endtype_counterparts(value)

    @property
    def export_installation_rectangular_materialization(self) -> bool:
        return self._level_of_detail.get_export_installation_rectangular_materialization()

    @export_installation_rectangular_materialization.setter
    def export_installation_rectangular_materialization(self, value: bool) -> None:
        self._level_of_detail.set_export_installation_rectangular_materialization(value)

    @property
    def export_end_type_materialization(self) -> bool:
        return self._level_of_detail.get_export_endtype_materialization()

    @export_end_type_materialization.setter
    def export_end_type_materialization(self, value: bool) -> None:
        self._level_of_detail.set_export_endtype_materialization(value)

    @property
    def export_installation_round_materialization(self) -> bool:
        return self._level_of_detail.get_export_installation_round_materialization()

    @export_installation_round_materialization.setter
    def export_installation_round_materialization(self, value: bool) -> None:
        self._level_of_detail.set_export_installation_round_materialization(value)

    @property
    def cut_drilling(self):
        return self._level_of_detail.get_cut_drillings()

    @cut_drilling.setter
    def cut_drilling(self, value: bool) -> None:
        self._level_of_detail.set_cut_drillings(value)
