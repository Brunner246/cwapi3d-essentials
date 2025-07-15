# Framework Independence

### Adapter für cwapi3d

```python
# Adapter-Klasse für die cwapi3d
class CwApi3dAdapter:
    @staticmethod
    def get_all_elements():
        import element_controller as ec
        return ec.get_visible_identifiable_element_ids()

    @staticmethod
    def get_element_name(element_id):
        import attribute_controller as ac
        # In einer realen Anwendung würde hier der tatsächliche Name abgerufen
        return ac.get_name(element_id) or f"Element {element_id}"

    @staticmethod
    def get_element_type(element_id):
        import utility_controller as uc
        # Element-Typ abrufen
        return uc.get_element_type_description(element_id)

    @staticmethod
    def activate_elements(element_ids):
        import element_controller as ec
        ec.set_active(element_ids)

    @staticmethod
    def deactivate_elements(element_ids):
        import element_controller as ec
        ec.set_inactive(element_ids)
```

### Angepasstes Model mit dem Adapter

```python
class CadElement:
    def __init__(self, element_id):
        self._element_id = element_id
        self._name = CwApi3dAdapter.get_element_name(element_id)
        self._element_type = CwApi3dAdapter.get_element_type(element_id)
        
    @property
    def element_id(self):
        return self._element_id
    
    ...



```

### Angepasstes ViewModel

```python
class CadElementViewModel(QObject):
    elementsChanged = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._elements = []
        self._load_elements()

    def _load_elements(self):
        element_ids = CwApi3dAdapter.get_all_elements()
        self._elements = [CadElement(id) for id in element_ids]
        self.elementsChanged.emit()
```

Durch die Verwendung eines Adapters wird eine saubere Trennung zwischen der cwapi3d und der MVVM-Architektur erreicht.
Dies erleichtert das Testen und ermöglicht eine einfachere Wartung der Anwendung.