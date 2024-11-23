from test.util import get_example_file


def test_parse44():
    from arxml_parse.autosar_00044 import Autosar
    from arxml_parse.io import parse_autosar_00044, serialize

    arxml_bytes = get_example_file("AUTOSAR_00044.xsd")
    root = parse_autosar_00044(arxml_bytes)
    assert isinstance(root, Autosar)
    xml_string = serialize(root)
    root = parse_autosar_00044(xml_string.encode())
    assert isinstance(root, Autosar)


def test_parse46():
    from arxml_parse.autosar_00046 import Autosar
    from arxml_parse.io import parse_autosar_00046, serialize

    arxml_bytes = get_example_file("AUTOSAR_00046.xsd")
    root = parse_autosar_00046(arxml_bytes)
    assert isinstance(root, Autosar)
    xml_string = serialize(root)
    root = parse_autosar_00046(xml_string.encode())
    assert isinstance(root, Autosar)


def test_parse48():
    from arxml_parse.autosar_00048 import Autosar
    from arxml_parse.io import parse_autosar_00048, serialize

    arxml_bytes = get_example_file("AUTOSAR_00048.xsd")
    root = parse_autosar_00048(arxml_bytes)
    assert isinstance(root, Autosar)
    xml_string = serialize(root)
    root = parse_autosar_00048(xml_string.encode())
    assert isinstance(root, Autosar)


def test_parse49():
    from arxml_parse.autosar_00049 import Autosar
    from arxml_parse.io import parse_autosar_00049, serialize

    arxml_bytes = get_example_file("AUTOSAR_00049.xsd")
    root = parse_autosar_00049(arxml_bytes)
    assert isinstance(root, Autosar)
    xml_string = serialize(root)
    root = parse_autosar_00049(xml_string.encode())
    assert isinstance(root, Autosar)


def test_parse50():
    from arxml_parse.autosar_00050 import Autosar
    from arxml_parse.io import parse_autosar_00050, serialize

    arxml_bytes = get_example_file("AUTOSAR_00050.xsd")
    root = parse_autosar_00050(arxml_bytes)
    assert isinstance(root, Autosar)
    xml_string = serialize(root)
    root = parse_autosar_00050(xml_string.encode())
    assert isinstance(root, Autosar)


def test_parse51():
    from arxml_parse.autosar_00051 import Autosar
    from arxml_parse.io import parse_autosar_00051, serialize

    arxml_bytes = get_example_file("AUTOSAR_00051.xsd")
    root = parse_autosar_00051(arxml_bytes)
    assert isinstance(root, Autosar)
    xml_string = serialize(root)
    root = parse_autosar_00051(xml_string.encode())
    assert isinstance(root, Autosar)


def test_parse52():
    from arxml_parse.autosar_00052 import Autosar
    from arxml_parse.io import parse_autosar_00052, serialize

    arxml_bytes = get_example_file("AUTOSAR_00052.xsd")
    root = parse_autosar_00052(arxml_bytes)
    assert isinstance(root, Autosar)
    xml_string = serialize(root)
    root = parse_autosar_00052(xml_string.encode())
    assert isinstance(root, Autosar)
