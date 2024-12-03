#!/bin/bash
# Bren-Square
# AoC 2024: Day 3

# Part 1
PROCESSED_TEXT="$(grep -oE 'mul\([[:digit:]]{1,3},[[:digit:]]{1,3}\)' input.txt)"

while IFS= read -r line; do
    read -r FIRST SECOND <<< "$(echo "$line" | sed -E 's/mul\(([0-9]{1,3}),([0-9]{1,3})\)/\1 \2/')"
    (( FINAL += FIRST * SECOND ))
done <<< "$PROCESSED_TEXT"

echo "Part 1: $FINAL"
unset FINAL

# Part 2
PROCESSED_TEXT="$(grep -o -e 'mul([[:digit:]]\{1,3\},[[:digit:]]\{1,3\})' -e "don't()" -e 'do()' input.txt)"
ENABLED='1'

while IFS= read -r line; do
    if [[ $line == "do()" ]]; then
        ENABLED='1'
    elif [[ $line == "don't()" ]]; then
        ENABLED='0'
    else
        if [[ $ENABLED == '1' ]]; then  
            read -r FIRST SECOND <<< "$(echo "$line" | sed -E 's/mul\(([0-9]{1,3}),([0-9]{1,3})\)/\1 \2/')"
            (( FINAL += FIRST * SECOND ))
        fi
    fi
done <<< "$PROCESSED_TEXT"

echo "Part 2: $FINAL"
