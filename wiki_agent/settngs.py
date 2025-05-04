from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    name = "wiki_agent"
    model = "gemini-2.0-flash-lite"
    # model = LiteLlm(model="ollama_chat/qwen3")
    description = "Wiki作成エージェント"
    root_instruction = "与えられたデータソースを分析して、Wikiを作成するエージェントです。"
    tree_instruction = """
        [fetch_file_tree]でファイルツリーを取得して箇条書きで出力してください。"
    """
    plan_instruction = """
        ファイルパスの一覧を踏まえつつ、最初に調べるファイルを3つ以内で選んでください。
    """
    source_instruction = """
        与えられたファイルパスからソースコードを取得してください。
        重要でなさそうな行は省略してください。
    """
    check_instruction = """
        与えられたファイル一覧やソースコードを分析して次の行動を決定してください。
        省略されている行でも必要があれば、再度取得してください。
    """
    markdown_instruction = """
        今までの調査結果の全てをMarkdown形式で整理し直して出力してください。
        依存関係が不明なものは省略してください。
    """
    mermaid_instruction = """
        今までの調査結果の全てをMermaid形式で整理し直して出力してください。
        依存関係が不明なものは省略してください。
    """
