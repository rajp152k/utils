# A basic timer

A basic timer.

## Usage 

Python 3.10+ as I'm using "|" instead of Unions when type hinting.
`aplay` to ring the alarm.

``` bash
alias timer "python3 /<path-to-parent-dir>/timer.py"

timer   -H <hours, default=0>   \
        -M <mins, default=0>    \
        -S <seconds, default=0> \
        -R <ring, default=<some file on my system, do change this>>
```
