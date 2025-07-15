from cadwork import ifc_options_properties


class IfcPropertyOptions:
    def __init__(self, parent: ifc_options_properties):
        self._property_options: ifc_options_properties = parent

    @property
    def attribute_nr_ifc_tag(self) -> int:
        return self._property_options.get_attriubte_nr_ifc_tag()

    @attribute_nr_ifc_tag.setter
    def attribute_nr_ifc_tag(self, value: int) -> None:
        self._property_options.set_attribute_nr_ifc_tag(value)

    @property
    def export_bim_wood_property(self) -> bool:
        return self._property_options.get_export_bim_wood_property()

    @export_bim_wood_property.setter
    def export_bim_wood_property(self, value: bool) -> None:
        self._property_options.set_export_bim_wood_property(value)

    @property
    def ignore_user_attributes_used_in_user_psets(self) -> bool:
        return self._property_options.get_ignore_user_attributes_used_in_psets()

    @ignore_user_attributes_used_in_user_psets.setter
    def ignore_user_attributes_used_in_user_psets(self, value: bool) -> None:
        self._property_options.set_ignore_user_attributes_used_in_psets(value)

    @property
    def export_cadwork_3d_pset(self) -> bool:
        return self._property_options.get_export_cadwork_3d_pset()

    @export_cadwork_3d_pset.setter
    def export_cadwork_3d_pset(self, value: bool) -> None:
        self._property_options.set_export_cadwork_3d_pset(value)

    @property
    def export_quantity_sets(self) -> bool:
        return self._property_options.get_export_quantity_sets()

    @export_quantity_sets.setter
    def export_quantity_sets(self, value: bool) -> None:
        self._property_options.set_export_quantity_sets(value)
