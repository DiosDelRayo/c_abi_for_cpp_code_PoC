#!/bin/bash
/home/thor/Qt/6.7.2/gcc_64/bin/qmake hash.pro
make
gcc -c main.c -o main.o
gcc main.o -L. -lhash -o main
LD_LIBRARY_PATH=. ./main
source bin/activate
python pochash.py
deactivate
