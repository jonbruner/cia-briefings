#!/bin/bash

for i in `seq 1961 1977`;
  do
    tar -czf documents/briefings_$i.tar.gz documents/Briefings_$i*
  done
