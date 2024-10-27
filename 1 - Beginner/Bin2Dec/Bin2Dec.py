# Binário para Decimal

"""
- - - - User Stories - - - -

- User can enter up to 8 binary digits in one input field
- User must be notified if anything other than a 0 or 1 was entered
- User views the results in a single output field containing the decimal (base 10)
  equivalent of the binary number that was entered

"""
import os


def limpa_tela():
    os.system('cls')


finished = False

while not finished:
    erro = {}
    try:
        binary_number = input("Informe um número binário: ")
        """
        if len(binary_number) > 8:
            erro["tamanho"] = "Valor deve ser no máximo 8 digitos."
            raise ValueError(erro["tamanho"])
    """

        if not ("0" in binary_number) or not ("1" in binary_number):
            erro["numero"] = "Por favor coloque apenas 0 ou 1."
            raise ValueError(erro["numero"])

        if not binary_number.isnumeric():
            erro["numerico"] = "O valor informado NÃO é numérico."
            raise ValueError(erro["numerico"])

        count = 0
        for enum, numero in enumerate(binary_number):
            res = int(numero) * pow(2, 10 - enum)
            count += res

        print(f"Binário: {binary_number}"
              f"\nDecimal: {count}")

    except ValueError as erro:
        print(erro)
    finally:
        finish_program = ''

        while finish_program not in ['0', '1']:
            finish_program = input("Deseja terminar o programa? \n"
                                   "SIM[1] NÃO[0]")

        finished = True if finish_program == '1' else False
        limpa_tela()