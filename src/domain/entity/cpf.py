import re
from ..exception.invalid_cpf import InvalidCpf

CPF_LENGTH = 11

class Cpf:
    """Class for validating data
    """
    def __init__(self, value: str):
        if not self.__validate(value):
            raise InvalidCpf
        self.__value = value

    @property
    def value(self):
        return self.__value

    def __remove_dashes_dots_and_whitespaces(self, cpf: str) -> str:
        """Remove all dashes and dots from the CPF, then trims the content

        Args:
            cpf (str): CPF

        Returns:
            str: trimmed CPF
        """
        return cpf.replace('-', '').replace('.', '').strip()

    def __validate_length(self, content: str, length: int) -> bool:
        """Check if the string contains exactly the length informed

        Args:
            content (str): string to be evaluated
            length (int): the expected length

        Returns:
            bool: True if the string has the expected length
        """
        return len(content) == length
     
    def __has_only_numbers(self, content: str) -> bool:
        """Check if the string received contains only numeric digits

        Args:
            content (str): string to be evaluated

        Returns:
            bool: True if contains only numeric digits
        """
        re_pattern = re.compile(r'^\d+$')
        return re.fullmatch(re_pattern, content) is not None

    def __calculate_checking_digit(self, cpf: str) -> str:
        digits_sum = 0
        length = len(cpf)
        for i in range(0, length):
            digits_sum += int(cpf[i]) * (length + 1 - i)
        checking_digit = CPF_LENGTH - (digits_sum % CPF_LENGTH)
        if checking_digit >= 10:
            return '0'
        return str(checking_digit)

    def __validate(self, cpf: str) -> bool:
        """Validate cpf string, containing no special chars

        Args:
            cpf (str): CPF about to be validated

        Returns:
            bool: True if CPF is valid
        """
        trimmed_cpf = self.__remove_dashes_dots_and_whitespaces(cpf)
        if not self.__validate_length(trimmed_cpf, CPF_LENGTH):
            return False
        if not self.__has_only_numbers(trimmed_cpf):
            return False
        first_digit = self.__calculate_checking_digit(trimmed_cpf[:-2])
        if first_digit != trimmed_cpf[-2]:
            return False
        second_digit = self.__calculate_checking_digit(trimmed_cpf[:-1])
        return second_digit == trimmed_cpf[-1]
