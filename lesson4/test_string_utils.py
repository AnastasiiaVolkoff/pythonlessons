import pytest
from string_utils import StringUtils


@pytest.fixture
def utils():
    return StringUtils()


# ---------- capitalize ----------
def test_capitalize_positive(utils):
    assert utils.capitalize("привет") == "Привет"
    assert utils.capitalize("hello world") == "Hello world"
    assert utils.capitalize("123abc") == "123abc"
    assert utils.capitalize(" уже есть пробел") == " уже есть пробел"


def test_capitalize_negative(utils):
    assert utils.capitalize("") == ""
    assert utils.capitalize(" ") == " "
    with pytest.raises(AttributeError):
        utils.capitalize(None)


# ---------- trim ----------
def test_trim_positive(utils):
    assert utils.trim("   skypro") == "skypro"
    assert utils.trim("skypro") == "skypro"
    assert utils.trim("   sky pro   ") == "sky pro   "
    assert utils.trim("") == ""


def test_trim_negative(utils):
    assert utils.trim(" ") == ""
    assert utils.trim("\t skypro") == "\t skypro"
    with pytest.raises(AttributeError):
        utils.trim(None)


# ---------- contains ----------
def test_contains_positive(utils):
    assert utils.contains("SkyPro", "S") is True
    assert utils.contains("SkyPro", "k") is True
    assert utils.contains("SkyPro", "Pro") is True
    assert utils.contains("12345", "3") is True


def test_contains_negative(utils):
    assert utils.contains("SkyPro", "U") is False
    assert utils.contains("", "a") is False
    assert utils.contains("abc", "") is False
    with pytest.raises(AttributeError):
        utils.contains(None, "a")
    with pytest.raises(AttributeError):
        utils.contains("abc", None)


# ---------- delete_symbol ----------
def test_delete_symbol_positive(utils):
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"
    assert utils.delete_symbol("aaaaa", "a") == ""
    assert utils.delete_symbol("", "a") == ""


def test_delete_symbol_negative(utils):
    assert utils.delete_symbol("SkyPro", "z") == "SkyPro"
    assert utils.delete_symbol("SkyPro", "") == "SkyPro"
    with pytest.raises(AttributeError):
        utils.delete_symbol(None, "a")
    with pytest.raises(AttributeError):
        utils.delete_symbol("abc", None)
