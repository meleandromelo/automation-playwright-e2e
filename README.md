#  Playwright E2E

[![Playwright E2E](https://github.com/meleandromelo/qa-portfolio-playwright-e2e/actions/workflows/playwright-tests.yml/badge.svg?branch=main)](https://github.com/meleandromelo/qa-portfolio-playwright-e2e/actions/workflows/playwright-tests.yml)

Oito testes de ponta a ponta verificam autenticação, formulários assíncronos, diálogos nativos do navegador e ordenação de dados no site de demonstração [The Internet](https://the-internet.herokuapp.com/).

A suíte usa Python, a API síncrona do Playwright e Pytest com `pytest-playwright`. Cada teste recebe um contexto isolado do Chromium. As ações aguardam os elementos ficarem disponíveis, e as asserções `expect` reavaliam a interface até que ela atinja o estado esperado. O resultado depende de acesso ao site público.

## Cobertura

| Caso | O que a suíte verifica |
| --- | --- |
| Login e logout | A conta de demonstração chega à área segura e recebe a confirmação de login. O logout volta ao formulário com a mensagem de saída. |
| Usuário inválido | O formulário informa que o nome de usuário é inválido e continua disponível. |
| Senha inválida | Uma senha errada para o usuário conhecido produz a mensagem específica de senha inválida. |
| Dynamic Loading | No exemplo 2, o título “Hello World!” só aparece no DOM após iniciar o carregamento. |
| Dynamic Controls | O checkbox é removido e adicionado novamente. O campo de texto aceita edição quando habilitado e conserva o valor depois de desabilitado. |
| Checkboxes e dropdown | O teste inverte as duas marcações e confirma os valores de duas seleções consecutivas no menu. |
| Diálogos JavaScript | Aceitar o alerta, cancelar a confirmação e responder ao prompt produz o tipo de diálogo, a mensagem e o resultado esperados. |
| Sortable Data Tables | O saldo é ordenado como valor monetário nos dois sentidos. A comparação das linhas completas verifica que cada saldo continua associado à pessoa correta. |

## Organização

| Caminho | Responsabilidade |
| --- | --- |
| `pages/` | Page Objects que localizam controles e encapsulam ações do usuário. |
| `tests/` | Cenários, dados de parametrização de falhas de login e asserções de comportamento. |
| `data/` | Credenciais públicas de demonstração exibidas pelo próprio site. |
| `pytest.ini` | Descoberta da suíte, URL de destino, navegador e retenção de evidências. |
| `results/` | Relatórios da execução e evidências de falha, gerados pelo Pytest. |
| `.vscode/` | Interpretador da pasta, descoberta de testes e recomendações de extensões. |
| `.github/workflows/` | Execução da suíte e upload dos resultados no GitHub Actions. |

## Executar no Windows

Com Python 3.15 instalado, clone o repositório e use o PowerShell na pasta do projeto.

```powershell
git clone https://github.com/meleandromelo/qa-portfolio-playwright-e2e.git
cd qa-portfolio-playwright-e2e
py -3.15 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m playwright install chromium
.\.venv\Scripts\python.exe -m pytest -v
```

O padrão é Chromium headless. Para acompanhar apenas a ordenação com a janela aberta:

```powershell
.\.venv\Scripts\python.exe -m pytest -v -k sort_balances --headed
```

### VS Code

Abra a pasta do repositório, instale as extensões recomendadas e prepare o ambiente com os comandos acima. A extensão **Python** descobre os oito casos no painel **Testing** e o **Pylance** oferece suporte à edição. Use **Refresh Tests** e **Run Tests** no painel. Se já houver outro interpretador selecionado, use **Python: Select Interpreter** e escolha `.venv\Scripts\python.exe`.

A extensão **Playwright Test for VS Code** também está nas recomendações. A descoberta e a execução desta suíte Python usam a integração do Pytest da extensão Python.

## Relatórios e diagnóstico de falhas

Abra `results/report.html` para ler o resultado por cenário. O arquivo `results/junit.xml` permite consumir o mesmo resultado em ferramentas de integração contínua.

Em caso de falha com uma página aberta, o plugin conserva a captura PNG e o `trace.zip` em `results/evidence/`. Para inspecionar ações, snapshots do DOM e chamadas de rede da falha, abra um trace da execução no visualizador local:

```powershell
$trace = Get-ChildItem .\results\evidence -Recurse -Filter trace.zip | Select-Object -First 1
.\.venv\Scripts\python.exe -m playwright show-trace $trace.FullName
```

Em cada push e pull request, o GitHub Actions instala o Chromium e suas dependências de sistema no Ubuntu e executa a suíte headless. O artefato **playwright-results** reúne os relatórios e eventuais evidências e fica disponível por 14 dias. [Ver execuções do workflow](https://github.com/meleandromelo/qa-portfolio-playwright-e2e/actions/workflows/playwright-tests.yml)
