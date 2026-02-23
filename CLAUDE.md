# プロジェクト概要

修士論文の研究用データ収集・整形プロジェクト。
Webスクレイピングや公開APIを利用して、自動車関連データおよびマクロ経済データを収集する。

関連リポジトリ: `D:\GitHub_Repository\Research\ma_thesis\`（論文本体・分析コード）

## 環境

- **OS**: Windows 11
- **Python**: 3.12（`.python-version` で指定）
- **パッケージ管理**: uv（`pyproject.toml` + `uv.lock`）
- **仮想環境**: `.venv/`（プロジェクトルート直下）
- **ブラウザ（Selenium用）**: Google Chrome + chromedriver
- **コマンド実行**: PowerShell / Git Bash

## ディレクトリ構成

```
Data/
├── scraping/
│   ├── oced_api.py              # OECD SDMX API ラッパー
│   ├── imf_api.py               # IMF REST API ラッパー
│   ├── selenium.ipynb            # Selenium 実験用ノートブック
│   ├── test.ipynb                # テスト用ノートブック
│   └── carview/                  # carview.yahoo.co.jp スクレイピング
│       ├── url/                  # 車種URL収集・集約
│       │   ├── car_url.json
│       │   ├── car_url_cleaned.json
│       │   ├── car_url_aggregated.json
│       │   └── url_aggregator.py
│       ├── codes/                # データ変換・整形
│       │   ├── car_charas.ipynb
│       │   ├── json_to_csv.ipynb
│       │   └── json_to_csv_nonev.ipynb
│       ├── scrape_car_attributes/    # 車両諸元スクレイピング
│       │   └── scrape.ipynb
│       └── scrape_consumer_attributes/  # 消費者属性スクレイピング
│           └── scrape.ipynb
├── selenium2.ipynb               # goo-net.com カタログスクレイピング
├── pyproject.toml
├── uv.lock
└── .venv/
```

## 主要ライブラリ

- **スクレイピング**: `selenium`, `undetected-chromedriver`, `requests`, `beautifulsoup4`
- **データ処理**: `pandas`
- **ノートブック**: `notebook`

## スクレイピング対象サイト

| サイト | 取得データ | 手法 |
|--------|-----------|------|
| carview.yahoo.co.jp | 車両諸元、消費者属性（年齢・年収・地域等） | Selenium（undetected-chromedriver） |
| goo-net.com | 車両カタログ情報（価格・燃費等） | requests + BeautifulSoup |
| OECD (sdmx.oecd.org) | マクロ経済統計 | REST API (requests) |
| IMF (dataservices.imf.org) | マクロ経済統計 | REST API (requests) |

## コーディング規約

- コメント・docstringは**日本語**で記述する
- 変数名・関数名は `snake_case`
- スクレイピングコードでは `robots.txt` を尊重し、適切な待機時間を設ける
- データの中間保存形式は JSON、最終出力は CSV

## .gitignore

Excel ファイル（`.xlsx`, `.xls` 等）と CSV ファイル（`.csv`）はGit管理外。
JSON ファイルはGit管理対象。

## コマンド例

```bash
# 依存パッケージのインストール
uv sync

# 仮想環境の有効化
.venv/Scripts/activate

# Jupyter Notebook の起動
jupyter notebook
```
