from abc import ABC


class ConceitoPessoa(ABC):
    def __init__(self, nome: str, cpf: str, data_nascimento: str):
        self.__nome = nome
        self.__cpf = cpf
        self.__data_nascimento = data_nascimento

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome) -> None:
        self.__nome = nome

    @property
    def cpf(self) -> str:
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf) -> None:
        self.__cpf = cpf

    @property
    def data_nascimento(self) -> str:
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento) -> None:
        self.__data_nascimento = data_nascimento
