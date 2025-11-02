# Diagrama-Pilha-Python
# Diagrama-Pilha-Python

[![CI](https://github.com/MarluciLeite/Diagrama-Pilha-Python/actions/workflows/ci.yml/badge.svg)](https://github.com/MarluciLeite/Diagrama-Pilha-Python/actions/workflows/ci.yml)
[![Coverage](https://codecov.io/gh/MarluciLeite/Diagrama-Pilha-Python/branch/main/graph/badge.svg)](https://codecov.io/gh/MarluciLeite/Diagrama-Pilha-Python)

Esqueleto de projeto Python para demonstrar uma implementação simples de pilha (stack), com testes e configurações mínimas para desenvolvimento no VS Code.

Como usar (Linux/macOS):

1. Crie e ative um ambiente virtual na raiz do projeto:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Instale dependências:

```bash
pip install -r requirements.txt
```

3. Rode os testes com pytest:

```bash
pytest -q
```

Arquivos importantes criados:

- `.gitignore` — regras de ignore para Python/VSCode
- `requirements.txt` — dependências (pytest)
- `src/pilha/stack.py` — implementação da pilha
- `tests/test_stack.py` — testes básicos com pytest
- `.vscode/settings.json` e `*.code-workspace` — configurações para VS Code

Se quiser que eu adicione um `devcontainer` para desenvolvimento em container, diga e eu adiciono.
