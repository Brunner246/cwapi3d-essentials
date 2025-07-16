# Zusammenfassung zur cwapi3d

## Inhaltsverzeichnis

1. [Einführung](#einführung)
2. [Aufbau der API](#aufbau-der-api)
3. [Logik hinter cwapi3d](#logik-hinter-cwapi3d)
4. [Projekteinrichtung](#projekteinrichtung)
    1. [Verzeichnisbekanntmachung](#verzeichnisbekanntmachung)
    2. [Verwendung mit 3rd-Party-Packages](#verwendung-mit-3rd-party-packages)
    3. [Projekte mit mehreren Dateien](#projekte-mit-mehreren-dateien)
5. [Verwendung der API](#verwendung-der-api)
6. [Referenzierung via Symlink](#referenzierung-via-symlink)

## Einführung

Die cwapi3d (cadwork API 3D) ist eine Python-Schnittstelle für cadwork 3d, die es ermöglicht, die Funktionalitäten von
cadwork über Python-Skripte zu erweitern und zu automatisieren. Die API stellt eine Verbindung zwischen Python und der
cadwork 3d-Software her und bietet Zugriff auf die Kernfunktionen des CAD-Systems.

Die cwapi3dpython ist auf GitHub
unter [https://github.com/cwapi3d/cwapi3dpython](https://github.com/cwapi3d/cwapi3dpython) verfügbar und kann über pip
installiert werden:

```bash
pip install cwapi3d
```

## Aufbau der API

Die cwapi3d-API ist modular aufgebaut und besteht aus verschiedenen Komponenten:

1. **Element-Manipulation**: Funktionen zum Erstellen, Bearbeiten und Löschen von cadwork-Elementen
2. **Attribute-Verwaltung**: Zugriff auf und Änderung von Elementattributen
3. **Geometrische Operationen**: Funktionen für Transformationen, Boolesche Operationen und geometrische Berechnungen
4. **Visualisierungstools**: Werkzeuge zur Darstellung und visuellen Manipulation
5. **Datei-I/O**: Import- und Exportfunktionen für verschiedene Dateiformate
6. **Utility-Funktionen**: Hilfsfunktionen für allgemeine Aufgaben

Die API folgt einer objektorientierten Struktur, wobei die meisten Funktionen über spezifische Module zugänglich sind,
die verschiedene Aspekte der cadwork-Funktionalität kapseln.

## Logik hinter cwapi3d

Die grundlegende Logik der cwapi3d basiert auf dem Konzept der Element-IDs. Jedes Element in cadwork hat eine eindeutige
ID, über die es identifiziert und manipuliert werden kann. Die API nutzt diese IDs als primären Mechanismus zur
Referenzierung von Elementen.

Der Workflow folgt typischerweise diesem Muster:

1. **Selektion**: Abrufen von Element-IDs durch direkte Auswahl oder Filter
2. **Manipulation**: Anwenden von Operationen auf die ausgewählten Elemente
3. **Eigenschaften setzen**: Ändern von Attributen wie Farbe, Material, usw.
4. **Visualisierung**: Aktualisieren der Anzeige, um Änderungen sichtbar zu machen

Die API verwendet ein Event-basiertes System für die Kommunikation mit cadwork und stellt sicher, dass Änderungen in der
3D-Umgebung korrekt reflektiert werden.

## Projekteinrichtung

### Verzeichnisbekanntmachung

Damit Python-Skripte in cadwork verwendet werden können, müssen sie im richtigen Verzeichnis platziert werden. Der
Standardpfad ist der `API.x64`-Ordner im Benutzerprofil.

Um diesen Ordner zu finden:

1. Öffnen Sie eine cadwork 3d-Datei
2. Navigieren Sie zu `Hilfe > Info`
3. Öffnen Sie den angezeigten Ordner namens `API.x64`

Für komplexere Projekte mit eigenen virtuellen Umgebungen, Paketmanagern wie Poetry oder mehreren Dateien müssen Sie
sicherstellen, dass cadwork Ihre Pakete und Module finden kann. Hierzu ist eine Anpassung des Python-Suchpfads
erforderlich.

### Verwendung mit 3rd-Party-Packages

Bei der Verwendung externer Python-Pakete gibt es verschiedene Ansätze:

1. **Verwendung von Poetry**: Wenn Sie Poetry verwenden, können Sie Ihre Abhängigkeiten in der `pyproject.toml`-Datei
   verwalten und die virtuelle Umgebung automatisch konfigurieren.
2. **Verwendung einer virtuellen Umgebung (venv)**: Sie können eine virtuelle Umgebung erstellen und diese in Ihrem
   Projekt verwenden, um Abhängigkeiten zu isolieren.

**Verwendung einer virtuellen Umgebung**:

   ```python
   import os
   import sys
   from pathlib import Path
   
   # Projektverzeichnis (Verzeichnis der aktuellen Datei)
   base_dir = Path(os.path.dirname(os.path.abspath(__file__)))
   src_dir = base_dir / "src"  # Falls vorhanden
   
   # Pfade, die zum Python-Suchpfad hinzugefügt werden sollen
   paths_to_add = [str(base_dir), str(src_dir)]
   
   # OPTION 1: Virtuelle Umgebung (venv) einbinden
   # Pfad zu Ihrer venv anpassen oder als None belassen, wenn nicht verwendet
   venv_path = None
   # Beispiele:
   # venv_path = Path("C:/Pfad/zu/meinem/venv") / "Lib" / "site-packages"  # Windows
   
   # OPTION 2: Poetry-Umgebung einbinden
   # Poetry-Umgebungsnamen anpassen oder als None belassen, wenn nicht verwendet
   poetry_venv_name = None
   # poetry_venv_name = "mein-projekt-py3.12-AbCdEfGh"  # Name Ihrer Poetry-Umgebung
   
   # Poetry-Umgebung automatisch finden, falls angegeben
   if poetry_venv_name:
       poetry_base = Path(os.environ.get("LOCALAPPDATA", "")) / "pypoetry" / "Cache" / "virtualenvs"
       site_packages = "Lib" / "site-packages"
   
       venv_path = poetry_base / poetry_venv_name / site_packages
   
   # Virtuelle Umgebung zum Suchpfad hinzufügen, falls vorhanden
   if venv_path and venv_path.exists():
       paths_to_add.insert(0, str(venv_path))  # Am Anfang einfügen für höhere Priorität
   
   # Alle Pfade zum Suchpfad hinzufügen
   for path in paths_to_add:
       if path not in sys.path and os.path.exists(path):
           sys.path.insert(0, path)
   
   # PYTHONPATH aktualisieren (optional, für Untermodule)
   existing_pythonpath = os.environ.get('PYTHONPATH', '')
   os.environ['PYTHONPATH'] = os.pathsep.join([*paths_to_add, existing_pythonpath])
   
   # Nach diesem Code können externe Module importiert werden
   # import meine_externen_pakete
   ```

Dieser Code sollte am Anfang Ihrer Hauptdatei stehen (z.B. in der `main.py` oder direkt in Ihrem cadwork-Skript).

### Projekte mit mehreren Dateien

Für Projekte mit mehreren Python-Dateien empfiehlt sich folgende Struktur:

1. **Modularer Aufbau**: Organisieren Sie Ihren Code in logische Module
2. **Package-Struktur**: Erstellen Sie ein Python-Package mit `__init__.py`-Dateien
3. **Relativer Import**: Verwenden Sie relative Imports zwischen Ihren Modulen

Eine empfohlene Projektstruktur:

```
mein_plugin/
├── __init__.py
├── main.py           # Haupteinstiegspunkt mit Pfadkonfiguration (wie oben)
├── src/              # Quellcode-Verzeichnis
│   ├── __init__.py
│   ├── models/       # Datenmodelle
│   │   ├── __init__.py
│   │   └── element.py
│   ├── adapters/     # Adapter für cwapi3d
│   │   ├── __init__.py
│   │   └── element_controller_wrapper.py
│   └── utils/        # Hilfsfunktionen
│       ├── __init__.py
│       └── geometry.py
└── pyproject.toml    # Bei Verwendung von Poetry
```

Nach der Pfadkonfiguration können Sie in Ihrer Hauptdatei Module wie folgt importieren:

```python
# In main.py nach der Pfadkonfiguration
from src.models.element import Element
from src.adapters.element_controller_wrapper import ElementControllerWrapper

# Oder innerhalb eines Moduls mit relativen Imports
from ..models.element import Element  # Innerhalb eines Adapters
```

## Verwendung der API

Die grundlegende Verwendung der cwapi3d erfolgt durch den Import der entsprechenden Module:

```python
import cadwork as cw
import utility_controller as uc

plugin_path = uc.get_plugin_path()
rhino_export_options = cw.rhino_options()
```

Ein typisches Skript könnte so aussehen:

```python
import cadwork as cw
import element_controller as ec
import attribute_controller as ac
import material_controller as mc
import visualization_controller as vc

# Elemente selektieren
element_ids = ec.get_active_identifiable_element_ids()

# Eigenschaften abfragen
for element_id in element_ids:
   name = ac.get_name(element_id)
   material_id = mc.get_material_id(ac.get_element_material_name(element_id))
   material = mc.get_name(material_id)
   print(f"Element: {name}, Material: {material}")

# Eigenschaften ändern
vc.set_color(element_ids, 5)
```

Die API bietet umfangreiche Funktionen für verschiedene Aufgaben, von einfachen Transformationen bis hin zu komplexen
geometrischen Operationen.

## Referenzierung via Symlink

Um ein Projekt via Symlink im `API.x64`-Verzeichnis zu referenzieren, können Sie folgendermaßen vorgehen:

### Windows

1. Öffnen Sie die Kommandozeile als Administrator
2. Verwenden Sie den `mklink`-Befehl, um einen symbolischen Link zu erstellen:

```cmd
mklink /D "C:\Users\[Benutzername]\cadwork\userprofil_[Version]\API.x64\mein_plugin" "C:\Pfad\zu\meinem\Entwicklungsordner\mein_plugin"
```

Dieser Ansatz hat mehrere Vorteile:

1. **Entwicklungsworkflow**: Sie können in Ihrer bevorzugten Entwicklungsumgebung arbeiten
2. **Versionskontrolle**: Einfache Integration mit Git oder anderen VCS
3. **Einfache Updates**: Änderungen werden sofort wirksam, ohne manuelle Kopien
4. **Projektorganisation**: Trennung von Entwicklungs- und Anwendungsumgebung

Beachten Sie, dass die cadwork-Anwendung nach einer Änderung möglicherweise neu gestartet werden muss, damit neue Module
erkannt werden.