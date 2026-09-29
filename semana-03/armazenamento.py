import json
from pathlib import Path

ARQUIVO = Path(__file__).with_name("solicitacoes.json")


def carregar() -> list[dict]:
    """Lê as solicitações salvas. Sem arquivo, começa com a lista vazia."""
    try:
        return json.loads(ARQUIVO.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return []


def salvar(solicitacoes: list[dict]) -> None:
    ARQUIVO.write_text(json.dumps(solicitacoes, ensure_ascii=False, indent=2), encoding="utf-8")
