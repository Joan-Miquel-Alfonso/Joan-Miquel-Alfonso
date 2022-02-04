#!/bin/bash
echo "executing: b_part.sh"
./b_part.sh &
wait
echo "executing: c_bash.sh"
./c_bash.sh > 911_2020_march-june_EMS_corregit.csv &
wait
echo "executing: c_awk.awk"
./c_awk.awk  911_2020_march-june_EMS_corregit.csv &
wait
echo "executing: d.sh"
./d.sh &
wait
echo "911_report.html has been created"
