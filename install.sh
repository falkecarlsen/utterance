#!/bin/bash

mkdir -p "$HOME/.config/utterance"

ln -s "$(realpath ./"utterance.py")" "$HOME/.config/utterance/"
touch "$HOME/.config/utterance/available"
touch "$HOME/.config/utterance/used"

echo "alias utter=\"python $HOME/.config/utterance/utterance.py\"" >> "$HOME/.bashrc"