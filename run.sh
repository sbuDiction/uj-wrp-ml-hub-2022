#!/bin/sh

a=0
while [ "$a" -lt 10 ]; do # this is loop1
    b="$a"
    while [ "$b" -ge 0 ]; do # this is loop2
        echo -n "$b "
        b=$(expr $b - 1)
    done
    echo
    a=$(expr $a + 1)
done
