from types import SimpleNamespace

from app import ask


def test_ask_prints_input_and_output_token_counts(monkeypatch, capsys):
    response = SimpleNamespace(
        usage_metadata=SimpleNamespace(prompt_token_count=12, candidates_token_count=5),
        text="answer",
    )
    client = SimpleNamespace(
        models=SimpleNamespace(generate_content=lambda **kwargs: response)
    )
    monkeypatch.setattr(ask, "get_api_key", lambda: "fake-key")
    monkeypatch.setattr(ask.genai, "Client", lambda **kwargs: client)

    assert ask.ask("question") == "answer"
    assert "[トークン] 入力: 12, 出力: 5" in capsys.readouterr().out