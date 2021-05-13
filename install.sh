#!/usr/bin/env bash

# Bus Pirate scripts installer

set -e

BIN_DIR="$HOME/bin"

pip3 install --no-cache-dir --user --progress-bar ascii -r requirements.txt
mkdir -p "$BIN_DIR"
cp -vf scripts/* "$BIN_DIR"

printf "Scripts installed.\n"
printf "\n\e[1;33mAdd %s to your PATH\e[0m\n\n" "$BIN_DIR"
