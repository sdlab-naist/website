#!/bin/bash

# --- 設定 ---
# ビルドするDockerイメージ名とタグ
IMAGE_NAME="sdlab-naist/hugo-dev"
IMAGE_TAG="0.84.1-go1.16"
FULL_IMAGE_NAME="${IMAGE_NAME}:${IMAGE_TAG}"
HOST_PORT="1313"
CONTAINER_PORT="1313"
DOCKERFILE="Dockerfile"
# --- 設定ここまで ---

# プロジェクトルートの取得
PROJECT_PATH=$(dirname "$(readlink -f "$0")")

# --- イメージビルド ---
echo "開発用Dockerイメージ $FULL_IMAGE_NAME をビルドします..."
docker build -t "$FULL_IMAGE_NAME" .
if [ $? -ne 0 ]; then
echo "エラー: Dockerイメージのビルドに失敗しました。"
exit 1
fi
echo "イメージのビルドが完了しました。"
# --- イメージビルドここまで ---

# --- 実行モードの分岐 ---
if [ "$#" -eq 0 ]; then
  # --- サーバモード (引数なし) ---
  echo "Hugo開発サーバーを起動します..."
  echo ""
  docker run --rm -it \
    -p "127.0.0.1:${HOST_PORT}:${CONTAINER_PORT}" \
    -v "${PROJECT_PATH}:/src" \
    -w "/src" \
    -u "$(id -u):$(id -g)" \
    "${FULL_IMAGE_NAME}" \
    hugo server --bind="0.0.0.0" --baseURL="http://localhost:${HOST_PORT}/" -DF
else
  # --- ワンライナーコマンドモード (引数あり) ---
  echo "引数 \"$@\" をコンテナ内で hugo コマンドとして実行します..."
  echo ""

  docker run --rm -it \
    -v "${PROJECT_PATH}:/src" \
    -w "/src" \
    -u "$(id -u):$(id -g)" \
    "${FULL_IMAGE_NAME}" \
    "$@" # スクリプトに渡された引数をそのままhugoの引数として渡して実行
fi

exit 0