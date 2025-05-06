from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    name = "wiki_agent"
    model = "gemini-2.0-flash-lite"
    # model = LiteLlm(model="ollama_chat/qwen3")
    description = "Wiki作成エージェント"
    root_instruction = "与えられたデータソースを分析して、Wikiを作成するエージェントです。"
    tree_instruction = """
        fetch_file_treeでファイルツリーを取得して箇条書きで出力してください。"
    """
    plan_instruction = """
        ファイルパスの一覧を踏まえつつ、最初に調べるファイルを3つ以内で選んでください。
        さらに、別の視点で調べたいキーワードを3つ以内で選んでください。
        JSON形式で出力してください。
        
        [フォーマット]
        {
          "files": {
            "ファイルパス１": "理由",
            "ファイルパス２": "理由",
            "ファイルパス３": "理由"
          },
          "keywords": {
            "キーワード１": "理由",
            "キーワード２": "理由",
            "キーワード３": "理由"
          }
        }
    """
    source_instruction = """
        与えられたファイルパスからソースコードを取得してください。
        重要でなさそうな行は省略してください。
    """
    check_instruction = """
        与えられたファイル一覧やソースコードを分析してMarkdown形式で整理し直して[markdown]に出力してください。
        さらに、次の行動をまとめて[next_actions]に出力してください。
        [markdown]と[next_actions]は合わせてJSON形式で出力してください。
        省略されている行でも必要があれば、再度取得してください。       
        
        [フォーマット]
        {
          "markdown": "Markdown形式で整理した内容",
          "next_actions": [
            "次の行動を3つ以内で挙げてください。",
            "例えば、「Aのファイルを詳しく調べる」といった内容です。",
          ]
        }
    """
    markdown_instruction = """
        今までの調査結果の全てを整理し直してMarkdownで出力してください。
        依存関係が不明なものは省略してください。

        [フォーマット]
        ## 目次
        - [概要](#概要)
        - [フローチャート](#フローチャート)
        - [クラス図](#クラス図)
        - [シーケンス図](#シーケンス図)
        
        ## 概要
        概要の内容
        
        ## フローチャート
        ユーザー視点でどんなことが実現できるかを記載する（不明ならなくても良い）
        ```mermaid
        graph LR
            StartA --> StopB;
            StartA --> StopC;
            
            subgraph BoxA
                StartC --> StopD
                StartE --> StopF
            end
            
            subgraph BoxB
                StartG --> StopH
                StartI --> StopJ
            end
        ```
        
        ## クラス図
        ```mermaid
        classDiagram
            class A {
                +method1()
                +method2()
            }
            class B {
                +method3()
                +method4()
            }
            A --|> B
            A --* C
        ```
        
        ## シーケンス図
        ```mermaid
        sequenceDiagram
            participant A
            participant B
            A ->> B:message1
            B ->> A:message2
            A ->> B:message3
        ```
        
        ## ER図
        DBなどを使っていれば記載する（不明ならなくても良い）
        ```mermaid
        erDiagram
            A {
                string aaa
                int bbb
            }
            B {
                string ccc
                int ddd
            }
            A ||--o{ B : note
        ```
    """
    evaluate_instruction = """
        あなたはこれまでの調査結果を知らない初学者の立場で評価してください。
        [generate_markdown_agent]または[update_markdown_agent]の出力を受け取り、以下のタスクに取り組んでください。
        JSON形式で出力してください。
    
        [タスク]
        A. 目次・概要・クラス図・シーケンス図があるかを確認してください。
        A. markdownの書式に誤りが無いか確認してください。
        B. mermaidでパース出来ない等の誤りが無いか[check_mermaid_format]ツールを用いて確認してください。（code=```mermaid\n...\n```）
        C. 改善するためのアイデアを3つ挙げてください。
        
        [フォーマット]
        {
          "evaluation": [
             "3つの文で出力に対する評価をしてください。",
             "各評価は1つの文で記述してください。",
             "例えば、「この部分はAのため良い」「ここはAのはずがBとなっており間違っている」といった内容です。"
          ],
          "improvements": [
             "ドキュメントとして改善するためのアイデアを3つ挙げてください。",
             "各アイデアは1つの文で記述してください。",
             "例えば、「この部分はもっと詳しく説明する必要がある」といった内容です。"
          ]
        }
    """
