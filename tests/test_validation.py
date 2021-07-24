import pytest
from ..src.validator import Validator

@pytest.fixture
def validator():
    return Validator()

def test_should_validate_correct_cpf(validator):
    assert validator.validate_cpf('30291840051')
    assert validator.validate_cpf('47465913004')
    assert validator.validate_cpf('03574151080')
    assert validator.validate_cpf('52632277019')
    assert validator.validate_cpf('12243951070')

def test_should_deny_incorrect_cpf(validator):
    assert validator.validate_cpf('46499458045') == False
    assert validator.validate_cpf('31195615093') == False
    assert validator.validate_cpf('40377045082') == False
    assert validator.validate_cpf('03239420040') == False
    assert validator.validate_cpf('20914218002') == False

def test_should_deny_cpf_with_wrong_length(validator):
    assert validator.validate_cpf('3029184005') == False
    assert validator.validate_cpf('302918400') == False
    assert validator.validate_cpf('30291840') == False
    assert validator.validate_cpf('3029184') == False
    assert validator.validate_cpf('302918') == False
    assert validator.validate_cpf('30291') == False
    assert validator.validate_cpf('3029') == False
    assert validator.validate_cpf('302') == False
    assert validator.validate_cpf('30') == False
    assert validator.validate_cpf('3') == False
    assert validator.validate_cpf('') == False
    assert validator.validate_cpf('302918400511') == False
    assert validator.validate_cpf('3029184005123') == False
    assert validator.validate_cpf('30291840051234') == False
    assert validator.validate_cpf('302918400512345') == False
    assert validator.validate_cpf('3029184005123456') == False
    assert validator.validate_cpf('30291840051234567') == False
    assert validator.validate_cpf('302918400512345678') == False
    assert validator.validate_cpf('3029184005123456789') == False
    assert validator.validate_cpf('30291840051234567890') == False

def test_should_deny_cpf_with_non_numeric_chars(validator):
    assert validator.validate_cpf('302918A0051') == False
    assert validator.validate_cpf('E0291840051') == False
    assert validator.validate_cpf('3029184005I') == False
    assert validator.validate_cpf('30291840O51') == False
    assert validator.validate_cpf('30291$40O51') == False

def test_should_validate_cpf_containing_dashes_and_dots(validator):
    assert validator.validate_cpf('157.823.860-96')
    assert validator.validate_cpf('101.203.370-88')
    assert validator.validate_cpf('046.960.300-32')
    assert validator.validate_cpf('858.664.030-13')
    assert validator.validate_cpf('753.394.110-10')

def test_should_validate_cpf_containing_trailing_whitespaces(validator):
    assert validator.validate_cpf('753.394.110-10 ')
    assert validator.validate_cpf('753.394.110-10  ')

def test_should_validate_cpf_containing_leading_whitespaces(validator):
    assert validator.validate_cpf('  753.394.110-10')
    assert validator.validate_cpf(' 753.394.110-10')
