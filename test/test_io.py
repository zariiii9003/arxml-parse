from test.util import get_example_file


def test_autosar_00044():
    from arxml_parse.autosar_00044 import Autosar
    from arxml_parse.io import parse_autosar_00044, serialize

    # get arxml path
    arxml_path = get_example_file("AUTOSAR_00044.xsd")

    # test parsing from file path
    root = parse_autosar_00044(arxml_path)
    assert isinstance(root, Autosar)

    # test parsing from file io
    with arxml_path.open("rt", encoding="utf-8") as arxml_file:
        root = parse_autosar_00044(arxml_file)
        assert isinstance(root, Autosar)

    # test parsing from string
    arxml_text = arxml_path.read_text("utf-8")
    root = parse_autosar_00044(arxml_text)
    assert isinstance(root, Autosar)

    # test serialization
    xml_string = serialize(root)
    root = parse_autosar_00044(xml_string)
    assert isinstance(root, Autosar)


def test_autosar_00046():
    from arxml_parse.autosar_00046 import Autosar
    from arxml_parse.io import parse_autosar_00046, serialize

    # get arxml path
    arxml_path = get_example_file("AUTOSAR_00046.xsd")

    # test parsing from file path
    root = parse_autosar_00046(arxml_path)
    assert isinstance(root, Autosar)

    # test parsing from file io
    with arxml_path.open("rt", encoding="utf-8") as arxml_file:
        root = parse_autosar_00046(arxml_file)
        assert isinstance(root, Autosar)

    # test parsing from string
    arxml_text = arxml_path.read_text("utf-8")
    root = parse_autosar_00046(arxml_text)
    assert isinstance(root, Autosar)

    # test serialization
    xml_string = serialize(root)
    root = parse_autosar_00046(xml_string)
    assert isinstance(root, Autosar)


def test_autosar_00048():
    from arxml_parse.autosar_00048 import Autosar
    from arxml_parse.io import parse_autosar_00048, serialize

    # get arxml path
    arxml_path = get_example_file("AUTOSAR_00048.xsd")

    # test parsing from file path
    root = parse_autosar_00048(arxml_path)
    assert isinstance(root, Autosar)

    # test parsing from file io
    with arxml_path.open("rt", encoding="utf-8") as arxml_file:
        root = parse_autosar_00048(arxml_file)
        assert isinstance(root, Autosar)

    # test parsing from string
    arxml_text = arxml_path.read_text("utf-8")
    root = parse_autosar_00048(arxml_text)
    assert isinstance(root, Autosar)

    # test serialization
    xml_string = serialize(root)
    root = parse_autosar_00048(xml_string)
    assert isinstance(root, Autosar)


def test_autosar_00049():
    from arxml_parse.autosar_00049 import Autosar
    from arxml_parse.io import parse_autosar_00049, serialize

    # get arxml path
    arxml_path = get_example_file("AUTOSAR_00049.xsd")

    # test parsing from file path
    root = parse_autosar_00049(arxml_path)
    assert isinstance(root, Autosar)

    # test parsing from file io
    with arxml_path.open("rt", encoding="utf-8") as arxml_file:
        root = parse_autosar_00049(arxml_file)
        assert isinstance(root, Autosar)

    # test parsing from string
    arxml_text = arxml_path.read_text("utf-8")
    root = parse_autosar_00049(arxml_text)
    assert isinstance(root, Autosar)

    # test serialization
    xml_string = serialize(root)
    root = parse_autosar_00049(xml_string)
    assert isinstance(root, Autosar)


def test_autosar_00050():
    from arxml_parse.autosar_00050 import Autosar
    from arxml_parse.io import parse_autosar_00050, serialize

    # get arxml path
    arxml_path = get_example_file("AUTOSAR_00050.xsd")

    # test parsing from file path
    root = parse_autosar_00050(arxml_path)
    assert isinstance(root, Autosar)

    # test parsing from file io
    with arxml_path.open("rt", encoding="utf-8") as arxml_file:
        root = parse_autosar_00050(arxml_file)
        assert isinstance(root, Autosar)

    # test parsing from string
    arxml_text = arxml_path.read_text("utf-8")
    root = parse_autosar_00050(arxml_text)
    assert isinstance(root, Autosar)

    # test serialization
    xml_string = serialize(root)
    root = parse_autosar_00050(xml_string)
    assert isinstance(root, Autosar)


def test_autosar_00051():
    from arxml_parse.autosar_00051 import Autosar
    from arxml_parse.io import parse_autosar_00051, serialize

    # get arxml path
    arxml_path = get_example_file("AUTOSAR_00051.xsd")

    # test parsing from file path
    root = parse_autosar_00051(arxml_path)
    assert isinstance(root, Autosar)

    # test parsing from file io
    with arxml_path.open("rt", encoding="utf-8") as arxml_file:
        root = parse_autosar_00051(arxml_file)
        assert isinstance(root, Autosar)

    # test parsing from string
    arxml_text = arxml_path.read_text("utf-8")
    root = parse_autosar_00051(arxml_text)
    assert isinstance(root, Autosar)

    # test serialization
    xml_string = serialize(root)
    root = parse_autosar_00051(xml_string)
    assert isinstance(root, Autosar)


def test_autosar_00052():
    from arxml_parse.autosar_00052 import Autosar
    from arxml_parse.io import parse_autosar_00052, serialize

    # get arxml path
    arxml_path = get_example_file("AUTOSAR_00052.xsd")

    # test parsing from file path
    root = parse_autosar_00052(arxml_path)
    assert isinstance(root, Autosar)

    # test parsing from file io
    with arxml_path.open("rt", encoding="utf-8") as arxml_file:
        root = parse_autosar_00052(arxml_file)
        assert isinstance(root, Autosar)

    # test parsing from string
    arxml_text = arxml_path.read_text("utf-8")
    root = parse_autosar_00052(arxml_text)
    assert isinstance(root, Autosar)

    # test serialization
    xml_string = serialize(root)
    root = parse_autosar_00052(xml_string)
    assert isinstance(root, Autosar)
