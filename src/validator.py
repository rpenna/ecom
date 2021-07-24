import re

class Validator:
    """Class for validating data
    """

    #def __remove_dashes_dots_and_whitespaces(self, cpf: str) -> str:
    #    return cpf.replace('-', '').replace('.', '').strip()
     
    def validate_cpf(self, cpf: str) -> bool:
        """Validate cpf string, containing no special chars

        Args:
            cpf (str): CPF about to be validated

        Returns:
            bool: True if CPF is valid
        """
        cpf = cpf.replace('-', '').replace('.', '').strip()
        if len(cpf) != 11:
            return False
        re_pattern = re.compile(r'^\d{11}$')
        if not re.fullmatch(re_pattern, cpf):
            return False
        soma = 0
        for i in range(0, 9):
            soma += int(cpf[i]) * (10 - i)
        digito1 = 11 - (soma % 11)
        if digito1 >= 10:
            digito1 = 0
        if str(digito1) != cpf[-2]:
            return False
        soma = 0
        for i in range(0, 10):
            soma += int(cpf[i]) * (11 - i)
        digito2 = 11 - (soma % 11)
        if digito2 >= 10:
            digito2 = 0
        return str(digito2) == cpf[-1]
