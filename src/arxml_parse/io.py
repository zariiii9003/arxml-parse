from pathlib import Path
from typing import IO, TYPE_CHECKING

from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

if TYPE_CHECKING:
    from typing import TypeAlias

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

    Autosar: TypeAlias = (
        Autosar00042
        | Autosar00043
        | Autosar00044
        | Autosar00045
        | Autosar00046
        | Autosar00047
        | Autosar00048
        | Autosar00049
        | Autosar00050
        | Autosar00051
        | Autosar00052
    )


def _read_arxml(arxml: Path | bytes | IO[bytes]) -> bytes:
    """Read ARXML content from the given input.

    :param arxml: The ARXML input, either a Path, bytes, or binary file-like object.
    :return: The content as bytes.
    :raises ValueError: If the input type is unsupported.
    """
    if isinstance(arxml, bytes):
        return arxml
    elif isinstance(arxml, Path):
        return arxml.read_bytes()
    elif hasattr(arxml, "read") and callable(arxml.read):
        return arxml.read()
    else:
        err_msg = (
            "Unsupported input type for 'arxml'. "
            "Must be Path, bytes, or a binary file-like object."
        )
        raise ValueError(err_msg)


def parse_autosar_00042(arxml: Path | bytes | IO[bytes]) -> "Autosar00042":
    """Parse an ARXML file conforming to AUTOSAR schema version 00042.

    :param arxml: The ARXML input, either a Path, bytes, or binary file-like object.
    :return: Parsed AUTOSAR 00042 object.
    """
    from .autosar_00042 import Autosar

    arxml_bytes = _read_arxml(arxml)
    root = XmlParser().from_bytes(arxml_bytes, Autosar)
    return root


def parse_autosar_00043(arxml: Path | bytes | IO[bytes]) -> "Autosar00043":
    """Parse an ARXML file conforming to AUTOSAR schema version 00043.

    :param arxml: The ARXML input, either a Path, bytes, or binary file-like object.
    :return: Parsed AUTOSAR 00043 object.
    """
    from .autosar_00043 import Autosar

    arxml_bytes = _read_arxml(arxml)
    root = XmlParser().from_bytes(arxml_bytes, Autosar)
    return root


def parse_autosar_00044(arxml: Path | bytes | IO[bytes]) -> "Autosar00044":
    """Parse an ARXML file conforming to AUTOSAR schema version 00044.

    :param arxml: The ARXML input, either a Path, bytes, or binary file-like object.
    :return: Parsed AUTOSAR 00044 object.
    """
    from .autosar_00044 import Autosar

    arxml_bytes = _read_arxml(arxml)
    root = XmlParser().from_bytes(arxml_bytes, Autosar)
    return root


def parse_autosar_00045(arxml: Path | bytes | IO[bytes]) -> "Autosar00045":
    """Parse an ARXML file conforming to AUTOSAR schema version 00045.

    :param arxml: The ARXML input, either a Path, bytes, or binary file-like object.
    :return: Parsed AUTOSAR 00045 object.
    """
    from .autosar_00045 import Autosar

    arxml_bytes = _read_arxml(arxml)
    root = XmlParser().from_bytes(arxml_bytes, Autosar)
    return root


def parse_autosar_00046(arxml: Path | bytes | IO[bytes]) -> "Autosar00046":
    """Parse an ARXML file conforming to AUTOSAR schema version 00046.

    :param arxml: The ARXML input, either a Path, bytes, or binary file-like object.
    :return: Parsed AUTOSAR 00046 object.
    """
    from .autosar_00046 import Autosar

    arxml_bytes = _read_arxml(arxml)
    root = XmlParser().from_bytes(arxml_bytes, Autosar)
    return root


def parse_autosar_00047(arxml: Path | bytes | IO[bytes]) -> "Autosar00047":
    """Parse an ARXML file conforming to AUTOSAR schema version 00047.

    :param arxml: The ARXML input, either a Path, bytes, or binary file-like object.
    :return: Parsed AUTOSAR 00047 object.
    """
    from .autosar_00047 import Autosar

    arxml_bytes = _read_arxml(arxml)
    root = XmlParser().from_bytes(arxml_bytes, Autosar)
    return root


def parse_autosar_00048(arxml: Path | bytes | IO[bytes]) -> "Autosar00048":
    """Parse an ARXML file conforming to AUTOSAR schema version 00048.

    :param arxml: The ARXML input, either a Path, bytes, or binary file-like object.
    :return: Parsed AUTOSAR 00048 object.
    """
    from .autosar_00048 import Autosar

    arxml_bytes = _read_arxml(arxml)
    root = XmlParser().from_bytes(arxml_bytes, Autosar)
    return root


def parse_autosar_00049(arxml: Path | bytes | IO[bytes]) -> "Autosar00049":
    """Parse an ARXML file conforming to AUTOSAR schema version 00049.

    :param arxml: The ARXML input, either a Path, bytes, or binary file-like object.
    :return: Parsed AUTOSAR 00049 object.
    """
    from .autosar_00049 import Autosar

    arxml_bytes = _read_arxml(arxml)
    root = XmlParser().from_bytes(arxml_bytes, Autosar)
    return root


def parse_autosar_00050(arxml: Path | bytes | IO[bytes]) -> "Autosar00050":
    """Parse an ARXML file conforming to AUTOSAR schema version 00050.

    :param arxml: The ARXML input, either a Path, bytes, or binary file-like object.
    :return: Parsed AUTOSAR 00050 object.
    """
    from .autosar_00050 import Autosar

    arxml_bytes = _read_arxml(arxml)
    root = XmlParser().from_bytes(arxml_bytes, Autosar)
    return root


def parse_autosar_00051(arxml: Path | bytes | IO[bytes]) -> "Autosar00051":
    """Parse an ARXML file conforming to AUTOSAR schema version 00051.

    :param arxml: The ARXML input, either a Path, bytes, or binary file-like object.
    :return: Parsed AUTOSAR 00051 object.
    """
    from .autosar_00051 import Autosar

    arxml_bytes = _read_arxml(arxml)
    root = XmlParser().from_bytes(arxml_bytes, Autosar)
    return root


def parse_autosar_00052(arxml: Path | bytes | IO[bytes]) -> "Autosar00052":
    """Parse an ARXML file conforming to AUTOSAR schema version 00052.

    :param arxml: The ARXML input, either a Path, bytes, or binary file-like object.
    :return: Parsed AUTOSAR 00052 object.
    """
    from .autosar_00052 import Autosar

    arxml_bytes = _read_arxml(arxml)
    root = XmlParser().from_bytes(arxml_bytes, Autosar)
    return root


def serialize(autosar_instance: "Autosar", indent: str = "  ") -> str:
    """Serialize an Autosar instance to an XML string.

    :param autosar_instance: An instance of an Autosar dataclass to be serialized.
    :param indent: Indent output by the given string.
    :return: A string containing the serialized XML representation.
    :raises ValueError: If the input is not a valid Autosar instance.
    """
    if autosar_instance.__class__.__name__ != "Autosar":
        err_msg = "The provided Autosar instance is invalid or None."
        raise ValueError(err_msg)

    config = SerializerConfig(indent=indent)
    serializer = XmlSerializer(config=config)
    return serializer.render(autosar_instance)
