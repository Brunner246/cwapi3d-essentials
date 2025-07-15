# Framework Independence

## Wrapper für cwapi3d

Ein Wrapper um die `cwapi3d` stellt eine abstrahierende Schicht zwischen deiner Anwendung und der API dar.
Dies erhöht die Unabhängigkeit deiner Anwendung von der cadwork-API und bietet zahlreiche Vorteile für eine nachhaltige
Softwareentwicklung.

### Vorteile eines Wrappers

1. **Abstraktion und Kapselung**:
    - Vereinfacht die komplexe cwapi3d zu einer anwendungsspezifischen Schnittstelle
    - Verbirgt die Implementierungsdetails und reduziert Abhängigkeiten

2. **Wartbarkeit**:
    - Änderungen an der cwapi3d betreffen nur den Wrapper, nicht die gesamte Anwendung
    - Leichtere Anpassung an API-Updates oder -Änderungen

3. **Testbarkeit**:
    - Einfachere Erstellung von Mock-Objekten für Unit-Tests
    - Bessere Testabdeckung ohne direkte Abhängigkeit von cadwork

4. **Anpassungsfähigkeit**:
    - Erweiterte Funktionalität ohne Änderung der Basis-API
    - Möglichkeit zur Implementierung anwendungsspezifischer Logik

5. **Typsicherheit**:
    - Konsistente Typdefinitionen und bessere IDE-Unterstützung
    - Reduzierung von Laufzeitfehlern durch statische Typprüfungen

### Nachteile eines Wrappers

1. **Zusätzliche Codeschicht**:
    - Erhöhter initialer Entwicklungsaufwand
    - Zusätzliche Wartungsebene im Projekt

2. **Potenzielle Performance-Einbussen**:
    - Geringfügiger Overhead durch zusätzliche Funktionsaufrufe
    - Mögliche Verzögerungen durch Konvertierungen zwischen Datentypen

3. **Synchronisierungsaufwand**:
    - Wrapper muss mit API-Updates synchron gehalten werden

## Beispiel-Implementierung eines Wrappers

```python
@dataclass
class ElementDimensions:
    width: float
    height: float
    length: float

    
@dataclass
class ElementAxisPoints:
    start: Point3D
    end: Point3D
    height: Point3D


# Wrapper-Klasse für die cwapi3d
class ElementControllerWrapper:
    @staticmethod
    def get_all_elements():
        import element_controller as ec
        return ec.get_visible_identifiable_element_ids()

    @staticmethod
    def get_element_name(element_id: int):
        import attribute_controller as ac
        return ac.get_name(element_id) or f"Element {element_id}"

    @staticmethod
    def create_rectangular_beam(dimensions: ElementDimensions, geometry: ElementAxisPoints):
       import element_controller as ec
       return ec.create_rectangular_beam_vectors(
           dimensions.width,
           dimensions.height,
           dimensions.length,
           to_cadwork_vector(geometry.start),
           to_cadwork_vector(geometry.end),
           to_cadwork_vector(geometry.height)
       )

```

## Projektstruktur mit Wrapper-Implementierung

```
project/
├── src/
│   └── adapters/                  # Wrapper für die cwapi3d
│       ├── __init__.py
│       ├── _utils.py              # Hilfsroutinen (z.B. Konvertierungen)
│       ├── element_controller_wrapper.py
│       ├── attribute_controller_wrapper.py
│       └── utility_controller_wrapper.py
│
├── tests/                         # Testfälle
│   ├── __init__.py
│   ├── test_element_wrapper.py    # Tests für den Wrapper
│   └── test_models.py             # Tests für die Modelle
│
└── docs/                          # Dokumentation
    ├── de/
    │   └── design.md
    └── examples/
        └── wrapper_usage.md
```

## Anwendungsbeispiel mit Wrapper

```python
# Verwendung des Wrappers in der Anwendung
class CadElement:
    def __init__(self, element_id):
        self._element_id = element_id
        self._name = ElementControllerWrapper.get_element_name(element_id)
        self._element_type = UtilityControllerWrapper.get_element_type(element_id)
        self._attributes = CadElementAttributes(element_id) # Annahme: CadElementAttributes ist eine Klasse, die Eigenschaften des Elements kapselt
        self._geometry = CadElementGeometry(element_id) # Annahme: CadElementGeometry ist eine Klasse, die Geometrie des Elements kapselt

    @property
    def element_id(self):
        return self._element_id
    
    @property
    def attributes(self):
        return self._attributes

```

Durch die Verwendung eines Wrappers wird eine klare Trennung zwischen der cwapi3d und der Anwendungslogik erreicht. Dies
führt zu besser wartbarem, testbarem und robusterem Code, der langfristig flexibler an Änderungen angepasst werden kann.