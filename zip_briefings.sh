#!/bin/bash

for i in `seq 1961 1974`;
  do
    tar -czf documents/briefings_$i.tar.gz documents/Briefings_$i*
  done

tar -czf documents/briefings_1975_1-6.tar.gz documents/Briefings_1975-01.pdf \
  documents/Briefings_1975-02.pdf documents/Briefings_1975-03.pdf \
  documents/Briefings_1975-04.pdf documents/Briefings_1975-05.pdf \
  documents/Briefings_1975-06.pdf

tar -czf documents/briefings_1975_7-12.tar.gz documents/Briefings_1975-07.pdf \
  documents/Briefings_1975-08.pdf documents/Briefings_1975-09.pdf \
  documents/Briefings_1975-10.pdf documents/Briefings_1975-11.pdf \
  documents/Briefings_1975-12.pdf

tar -czf documents/briefings_1976.tar.gz documents/Briefings_1976*

tar -czf documents/briefings_1977.tar.gz documents/Briefings_1977*
