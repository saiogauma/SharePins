# 作品No.01 SharePins


## 環境構築

1. ローカル環境に取り込む
```shell
git clone https://github.com/saiogauma/SharePins.git
```

2. 仮想環境の作成
```shell
python -m venv .venv
```

3. ライブラリのインストール
```shell
pip install -r requirements.txt
```

4. 環境変数(.envファイル)の編集
```python
GOOGLE_MAPS_API_KEY = '各自取得したAPIキーをセット'
```

5. サーバーの立ち上げ
```shell
python serve.py
```