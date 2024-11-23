from pathlib import Path
from typing import TYPE_CHECKING

from xsdata.formats.dataclass.parsers import XmlParser

if TYPE_CHECKING:
    from .autosar_00042 import Autosar as Autosar00042
    from .autosar_00043 import Autosar as Autosar00043
    from .autosar_00044 import Autosar as Autosar00044
    from .autosar_00045 import Autosar as Autosar00045
    from .autosar_00046 import Autosar as Autosar00046
    from .autosar_00047 import Autosar as Autosar00047
    from .autosar_00048 import Autosar as Autosar00048
    from .autosar_00049 import Autosar as Autosar00049
    from .autosar_00050 import Autosar as Autosar00050
    from .autosar_00051 import Autosar as Autosar00051
    from .autosar_00052 import Autosar as Autosar00052


def parse_autosar_00042(arxml: Path | bytes) -> "Autosar00042":
    from .autosar_00042 import Autosar

    arxml_bytes = arxml if isinstance(arxml, bytes) else arxml.read_bytes()
    root = XmlParser().from_bytes(arxml_bytes, Autosar)
    return root


def parse_autosar_00043(arxml: Path | bytes) -> "Autosar00043":
    from .autosar_00043 import Autosar

    arxml_bytes = arxml if isinstance(arxml, bytes) else arxml.read_bytes()
    root = XmlParser().from_bytes(arxml_bytes, Autosar)
    return root


def parse_autosar_00044(arxml: Path | bytes) -> "Autosar00044":
    from .autosar_00044 import Autosar

    arxml_bytes = arxml if isinstance(arxml, bytes) else arxml.read_bytes()
    root = XmlParser().from_bytes(arxml_bytes, Autosar)
    return root


def parse_autosar_00045(arxml: Path | bytes) -> "Autosar00045":
    from .autosar_00045 import Autosar

    arxml_bytes = arxml if isinstance(arxml, bytes) else arxml.read_bytes()
    root = XmlParser().from_bytes(arxml_bytes, Autosar)
    return root


def parse_autosar_00046(arxml: Path | bytes) -> "Autosar00046":
    from .autosar_00046 import Autosar

    arxml_bytes = arxml if isinstance(arxml, bytes) else arxml.read_bytes()
    root = XmlParser().from_bytes(arxml_bytes, Autosar)
    return root


def parse_autosar_00047(arxml: Path | bytes) -> "Autosar00047":
    from .autosar_00047 import Autosar

    arxml_bytes = arxml if isinstance(arxml, bytes) else arxml.read_bytes()
    root = XmlParser().from_bytes(arxml_bytes, Autosar)
    return root


def parse_autosar_00048(arxml: Path | bytes) -> "Autosar00048":
    from .autosar_00048 import Autosar

    arxml_bytes = arxml if isinstance(arxml, bytes) else arxml.read_bytes()
    root = XmlParser().from_bytes(arxml_bytes, Autosar)
    return root


def parse_autosar_00049(arxml: Path | bytes) -> "Autosar00049":
    from .autosar_00049 import Autosar

    arxml_bytes = arxml if isinstance(arxml, bytes) else arxml.read_bytes()
    root = XmlParser().from_bytes(arxml_bytes, Autosar)
    return root


def parse_autosar_00050(arxml: Path | bytes) -> "Autosar00050":
    from .autosar_00050 import Autosar

    arxml_bytes = arxml if isinstance(arxml, bytes) else arxml.read_bytes()
    root = XmlParser().from_bytes(arxml_bytes, Autosar)
    return root


def parse_autosar_00051(arxml: Path | bytes) -> "Autosar00051":
    from .autosar_00051 import Autosar

    arxml_bytes = arxml if isinstance(arxml, bytes) else arxml.read_bytes()
    root = XmlParser().from_bytes(arxml_bytes, Autosar)
    return root


def parse_autosar_00052(arxml: Path | bytes) -> "Autosar00052":
    from .autosar_00052 import Autosar

    arxml_bytes = arxml if isinstance(arxml, bytes) else arxml.read_bytes()
    root = XmlParser().from_bytes(arxml_bytes, Autosar)
    return root
