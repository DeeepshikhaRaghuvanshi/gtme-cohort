#!/usr/bin/env bash
# Fetch the local text-to-speech tools used by video/render3.py (not stored in git).
# Linux x86_64. Needs curl and tar; rendering also needs ffmpeg on PATH.
set -euo pipefail
cd "$(dirname "$0")/../video"

if [ ! -x piper/piper ]; then
  curl -fsSL -o piper.tar.gz "https://github.com/rhasspy/piper/releases/download/2023.11.14-2/piper_linux_x86_64.tar.gz"
  tar -xzf piper.tar.gz && rm piper.tar.gz
fi

mkdir -p voice
base="https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/lessac/medium"
[ -f voice/en_US-lessac-medium.onnx ] || curl -fsSL -o voice/en_US-lessac-medium.onnx "$base/en_US-lessac-medium.onnx"
[ -f voice/en_US-lessac-medium.onnx.json ] || curl -fsSL -o voice/en_US-lessac-medium.onnx.json "$base/en_US-lessac-medium.onnx.json"

command -v ffmpeg >/dev/null || echo "Warning: ffmpeg not found; install it before running render3.py clips/final."
echo "Ready. Render with: python3 render3.py stills|audio|clips|final (run from video/)"
