#!/bin/bash
# Bren-Square
# AoC 2024: Day 3

# Part 1

# Get mul values
PROCESSED_TEXT="$(grep -oE 'mul\([[:digit:]]{1,3},[[:digit:]]{1,3}\)' input.txt)"

# loopity-loop
while IFS= read -r line; do
    # extract first and second digits
    read -r FIRST SECOND <<< "$(echo "$line" | sed -E 's/mul\(([0-9]{1,3}),([0-9]{1,3})\)/\1 \2/')"
    # Add them together into a variable for later
    (( FINAL += FIRST * SECOND ))
done <<< "$PROCESSED_TEXT"

# print value
echo "Part 1: $FINAL"

# unset for part 2
unset FINAL

# Part 2

# Get muls, dos, and don'ts
PROCESSED_TEXT="$(grep -o -e 'mul([[:digit:]]\{1,3\},[[:digit:]]\{1,3\})' -e "don't()" -e 'do()' input.txt)"
# Set initial enable
ENABLED='1'

# more loops
while IFS= read -r line; do
    if [[ $line == "do()" ]]; then
        ENABLED='1'
    elif [[ $line == "don't()" ]]; then
        ENABLED='0'
    else
        # same logic as before except we only run this when enabled is true and it's not a do/dont
        if [[ $ENABLED == '1' ]]; then  
            read -r FIRST SECOND <<< "$(echo "$line" | sed -E 's/mul\(([0-9]{1,3}),([0-9]{1,3})\)/\1 \2/')"
            (( FINAL += FIRST * SECOND ))
        fi
    fi
done <<< "$PROCESSED_TEXT"

# spit out the answer
echo "Part 2: $FINAL"
