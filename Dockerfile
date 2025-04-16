# ビルドステージ
FROM golang:1.16-alpine

# HUGOのバージョン指定
ARG HUGO_VERSION=0.84.1

# 必要なビルドツール
RUN apk add --no-cache git g++ musl-dev libstdc++ ca-certificates

# Hugo extended をソースからビルド
ENV CGO_ENABLED=1
RUN go install -tags extended github.com/gohugoio/hugo@v${HUGO_VERSION}

WORKDIR /src
EXPOSE 1313

# デフォルトコマンド
CMD ["hugo version"]
