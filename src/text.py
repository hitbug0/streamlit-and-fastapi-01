import dataclasses


@dataclasses.dataclass
class Text:
    TITLE: str
    DESCRIPTIONS: list[str]
    FIGURES: list[str]


TITLE = """
# Streamlit and FastAPI Integration
フロントエンドを `Streamlit`、バックエンドを `FastAPI` で実装した簡単なWebアプリです。

ローカルに立てた両サーバの接続を確認できます。
"""


ABOUT_STREAMLIT = """
## 特徴
- 迅速に開発できる
    - UIコンポーネンツが一通りそろっており、UIを簡単に整えられる
    - コードを変更すると自動でリロードしてくれる
- Markdown記法に対応している
    - streamlit_mermaid を使えば mermaid による作図もできる
- [Components - Streamlit](https://streamlit.io/components) にカスタムテンプレートが公開されている。
- GitHub経由でインターネット上にアプリを公開できる
- ライセンス: Apache License 2.0

## 主なユースケース
- プロトタイピング、データ可視化、インタラクティブなダッシュボードの作成を迅速に行いたい場合
    - データサイエンスや機械学習のプロジェクトとか
- UI作成が主な目的で、バックエンドの複雑な処理は他のサービスに任せる場合

## 仕様
- [API Reference - Streamlit Docs](https://docs.streamlit.io/develop/api-reference) を参照。

## 参考記事
- [ChatGPTとMermaidで、SnowflakeのER図を描かせてみた](https://qiita.com/Itsuki_Inoue/items/465bbad13bbc942fe7aa)
"""


ABOUT_FASTAPI = """
## 特徴
- ASGI（Asynchronous Server Gateway Interface）標準に基づいており、高速
- Flaskと同じような書き方なので、勉強すると応用できるかも。
    - [Python製WebフレームワークをFlaskからFastAPIに変えた話](https://note.com/navitime_tech/n/nc0381517d067)
- [APIリファレンス]({SERVER_URL}/docs) を自動で作ってくれる。
    - Pythonの型ヒントを利用
- Pydanticを利用し、データを自動バリデーションできる
- ライセンス: MIT

## 主なユースケース
- 高速なパフォーマンスが求められるWeb APIの構築
- 非同期処理を活用したスケーラブルなアプリケーションの開発
"""


FIG1 = """
sequenceDiagram
    actor User as User
    participant Browser as Web Browser
    participant Server as Backend Server

    User->>Browser: Clicks button
    Browser->>Server: Sends GET request
    Server-->>Browser: Returns response
    Browser-->>User: Displays response on screen
"""


text = Text(
    TITLE,
    [
        ABOUT_STREAMLIT,
        ABOUT_FASTAPI,
    ],
    [FIG1],
)
