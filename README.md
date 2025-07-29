Projeto de Testes Automatizados com Pytest – Aula 2
Este projeto faz parte da Aula 2 do curso prático de QA com Python e Pytest.
O foco é criar testes automatizados parametrizados e utilizar a ferramenta pytest-cov para análise de cobertura de testes.

📁 Estrutura do Projeto
Copiar
Editar
qa_aula2/
├── codigo/
│   └── calculos.py
├── testes/
│   ├── test_calculos.py
│   └── Resultado_cobertura.txt
└── README.md
📦 Requisitos
Python 3.11+ (usado neste projeto: 3.13.5)

pytest

pytest-cov

Instalar as dependências:
bash
Copiar
Editar
pip install pytest pytest-cov
✅ Funcionalidades testadas
O projeto implementa duas funções simples em calculos.py:

python
Copiar
Editar
def dividir(a, b):
    return a / b

def eh_par(numero):
    return numero % 2 == 0
🧪 Executando os testes
Testes com saída detalhada:
bash
Copiar
Editar
pytest -v testes/
Testes com relatório de cobertura de código:
bash
Copiar
Editar
pytest --cov=codigo testes/ > testes/Resultado_cobertura.txt
📄 Exemplo de saída esperada no arquivo Resultado_cobertura.txt
markdown
Copiar
Editar
Name                 Stmts   Miss  Cover
----------------------------------------
codigo\__init__.py       0      0   100%
codigo\calculos.py       4      0   100%
----------------------------------------
TOTAL                    4      0   100%
⚠️ Observações
A função eh_par() foi ajustada após os primeiros testes falharem com retorno None. A função corrigida retorna corretamente True ou False.

Todos os testes estão parametrizados para garantir cobertura com diferentes cenários.

📚 Próximos passos sugeridos
Adicionar tratamento de exceções em dividir para divisão por zero.

Explorar pytest.raises para testes de erros.

Implementar testes com mock e fixtures nas próximas aulas.

🧑‍💻 Autor
César Henrique da Silva
Projeto desenvolvido para fins didáticos e de portfólio.
