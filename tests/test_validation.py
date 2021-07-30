import pytest
from ..src.cpf import Cpf
from ..src.invalid_cpf import InvalidCpf

valid_cpf = (
    '30291840051',
    '47465913004',
    '03574151080',
    '52632277019',
    '12243951070',
)

invalid_cpf = (
    '46499458045',
    '31195615093',
    '40377045082',
    '03239420040',
    '20914218002',
)

wrong_length_cpf = (
    '3029184005',
    '302918400',
    '30291840',
    '3029184',
    '302918',
    '30291',
    '3029',
    '302',
    '30',
    '3',
    '',
    '302918400511',
    '3029184005123',
    '30291840051234',
    '302918400512345',
    '3029184005123456',
    '30291840051234567',
    '302918400512345678',
    '3029184005123456789',
    '30291840051234567890',
)

non_numeric_chars_cpf = (
    '302918A0051',
    'E0291840051',
    '3029184005I',
    '30291840O51',
    '30291$40O51',
)

cpf_with_dashes_and_dots = (
    '753.394.110-10',
    '157.823.860-96',
    '101.203.370-88',
    '046.960.300-32',
    '858.664.030-13',
)

trailing_whitespaces = (
    '753.394.110-10 ',
    '753.394.110-10  ',
)

leading_whitespaces = (
    '  753.394.110-10',
    ' 753.394.110-10',
)


@pytest.mark.parametrize(
    'valid_cpf',
    valid_cpf
)
def test_should_validate_correct_cpf(valid_cpf):
    try:
        Cpf(valid_cpf)
    except InvalidCpf:
        pytest.fail('Unexpected InvalidCpf raised')

@pytest.mark.parametrize(
    'invalid_cpf',
    invalid_cpf
)
def test_should_deny_incorrect_cpf(invalid_cpf):
    with pytest.raises(InvalidCpf):
        Cpf(invalid_cpf)

@pytest.mark.parametrize(
    'wrong_length_cpf',
    wrong_length_cpf
)
def test_should_deny_cpf_with_wrong_length(wrong_length_cpf):
    with pytest.raises(InvalidCpf):
        Cpf(wrong_length_cpf)

@pytest.mark.parametrize(
    'non_numeric_chars_cpf',
    non_numeric_chars_cpf
)
def test_should_deny_cpf_with_non_numeric_chars(non_numeric_chars_cpf):
    with pytest.raises(InvalidCpf):
        Cpf(non_numeric_chars_cpf)

@pytest.mark.parametrize(
    'cpf_with_dashes_and_dots',
    cpf_with_dashes_and_dots
)
def test_should_validate_cpf_containing_dashes_and_dots(cpf_with_dashes_and_dots):
    try:
        Cpf(cpf_with_dashes_and_dots)
    except InvalidCpf:
        pytest.fail('Unexpected InvalidCpf raised')

@pytest.mark.parametrize(
    'trailing_whitespaces',
    trailing_whitespaces
)
def test_should_validate_cpf_containing_trailing_whitespaces(trailing_whitespaces):
    try:
        Cpf(trailing_whitespaces)
    except InvalidCpf:
        pytest.fail('Unexpected InvalidCpf raised')

@pytest.mark.parametrize(
    'leading_whitespaces',
    leading_whitespaces
)
def test_should_validate_cpf_containing_leading_whitespaces(leading_whitespaces):
    try:
        Cpf(leading_whitespaces)
    except InvalidCpf:
        pytest.fail('Unexpected InvalidCpf raised')
