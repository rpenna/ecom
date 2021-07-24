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
    assert validator.validate_cpf('46499458045')
    assert validator.validate_cpf('31195615093')
    assert validator.validate_cpf('40377045082')
    assert validator.validate_cpf('03239420040')
    assert validator.validate_cpf('20914218002')

def test_should_deny_cpf_with_wrong_length(validator):
    assert validator.validate_cpf('3029184005')
    assert validator.validate_cpf('302918400')
    assert validator.validate_cpf('30291840')
    assert validator.validate_cpf('3029184')
    assert validator.validate_cpf('302918')
    assert validator.validate_cpf('30291')
    assert validator.validate_cpf('3029')
    assert validator.validate_cpf('302')
    assert validator.validate_cpf('30')
    assert validator.validate_cpf('3')
    assert validator.validate_cpf('')
    assert validator.validate_cpf('302918400511')
    assert validator.validate_cpf('3029184005123')
    assert validator.validate_cpf('30291840051234')
    assert validator.validate_cpf('302918400512345')
    assert validator.validate_cpf('3029184005123456')
    assert validator.validate_cpf('30291840051234567')
    assert validator.validate_cpf('302918400512345678')
    assert validator.validate_cpf('3029184005123456789')
    assert validator.validate_cpf('30291840051234567890')

def test_should_deny_cpf_with_non_numeric_chars(validator):
    assert validator.validate_cpf('302918A0051')
    assert validator.validate_cpf('E0291840051')
    assert validator.validate_cpf('3029184005I')
    assert validator.validate_cpf('30291840O51')
    assert validator.validate_cpf('30291$40O51')
