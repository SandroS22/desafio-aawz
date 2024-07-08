# Desafio-aawz

`python: 3.10.12`

`SQLite3`

Primeiramente altere o caminho para o banco de dados no arquivo `AppRepository.py` inserirndo o caminho para o seu banco
de dados SQLite

Caso não haja dados nos banco, rode o script `inserir_vendas.py` e o `inserir_vendedores.py`.

Endpoints:

/home: caminho raiz, apenas com uma mensagem de bem-vindo.

/vendedor: ao colocar inserir a variável id_vendedor no corpo da requisição, retorna o vendedor caso ele exista.

/vendedores/apagar_vendedor: apaga um vendedor passado o id no corpo da requisição.

/vendedores/novo_vendedor: cria um novo vendedor

/comissoes: retorna a comissão e média de venda de cada vendedor

Ficou faltando a implementação do update.

Para rodar o programa, basta ter o flask instalado, ir na raiz do projeto e passar o seguinte comando no
terminal: `python3 -m flask run`