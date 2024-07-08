from Enumerators.TipoEstado import TipoEstado
from Repositories import AppRepository


class AppController:
    def cadastrar_vendedor(self, nome: str, cpf: str, data_nascimento: str, email: str, estado: TipoEstado):
        return AppRepository.cadastrar_vendedor(nome, cpf, data_nascimento, email, estado)

    def get_vendedores(self):
        return AppRepository.get_vendedores()

    def get_vendedor(self, id: int):
        return AppRepository.get_vendedor(id)

    def apagar_vendedor(self, id: int):
        return AppRepository.apagar_vendedor(id)

    def get_vendas(self):
        return AppRepository.vendas()

    def calcula_comissao(self):
        # Isso ta muito feio, da para melhorar
        vendedores = {}
        for vendedor in self.get_vendedores().json:
            comissao = 0
            vendas_online = {'qtd': 0, 'valor': 0}
            vendas_telefone = {'qtd': 0, 'valor': 0}
            vendas_loja = {'qtd': 0, 'valor': 0}
            for venda in self.get_vendas().json:
                if vendedor.get('nome') == venda.get('nome_vendedor'):
                    if venda.get('canal_venda') == "Online":
                        vendas_online['qtd'] += 1
                        vendas_online['valor'] += venda.get('valor_venda')
                        comissao_temp = venda.get('valor_venda') * 0.1
                        comissao += comissao_temp * 0.8
                    if venda.get('canal_venda') == "Telefone":
                        vendas_telefone['qtd'] += 1
                        vendas_telefone['valor'] += venda.get('valor_venda')
                        comissao += venda.get('valor_venda') * 0.1
                    if venda.get('canal_venda') == "Loja física":
                        vendas_loja['qtd'] += 1
                        vendas_loja['valor'] += venda.get('valor_venda')
                        comissao += venda.get('valor_venda') * 0.1
                media_online = 0
                media_telefone = 0
                media_loja = 0
                if vendas_online['qtd'] > 0:
                    media_online = vendas_online['valor'] / vendas_online['qtd']

                if vendas_telefone['qtd'] > 0:
                    media_telefone = vendas_telefone['valor'] / vendas_telefone['qtd']
                if vendas_loja['qtd'] > 0:
                    media_loja = vendas_loja['valor'] / vendas_loja['qtd']
                vendedores[vendedor.get('nome')] = {'comissao': float(format(comissao, ".2f")),
                                                    'media_online': float(format(media_online, ".2f")),
                                                    'media_telefone': float(format(media_telefone, ".2f")),
                                                    'media_loja': float(format(media_loja, ".2f"))}
            if comissao > 1000:
                vendedores['comissao'] = comissao - (comissao * 0.1)
        return vendedores
