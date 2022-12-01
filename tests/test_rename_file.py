from RP2MD.html_parser import rename_output_file


def test_rename():
    assert rename_output_file("Hello-Name") == "Hello name"

