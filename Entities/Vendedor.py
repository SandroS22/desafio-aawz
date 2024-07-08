from Entities.ConceitoPessoa import ConceitoPessoa
from Enumerators.TipoEstado import TipoEstado


class Vendedor(ConceitoPessoa):
    def __init__(self, nome, cpf: str, data_nascimento: str, email: str, estado: TipoEstado):
        super().__init__(nome, cpf, data_nascimento)
        self.__email = email
        self.__estado = estado

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email) -> None:
        self.__email = email

    @property
    def estado(self) -> TipoEstado:
        return self.__estado

    @estado.setter
    def estado(self, estado) -> None:
        if isinstance(estado, TipoEstado):
            self.__estado = estado
        else:
            raise TypeError("Estado invalido")

    def __str__(self):
        return self.nome
