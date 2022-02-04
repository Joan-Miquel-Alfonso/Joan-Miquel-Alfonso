#!/bin/awk -f
BEGIN {FS=",";OFS=","}
{if (NR>1 && $10!="NULL" && $11!="NULL"){arr[$11]++}}
END {PROCINFO["sorted_in"]="@ind_num_asc"; for (a in arr) print a, arr[a], arr[a]/85 > "total_calls_by_hour.csv" }
BEGIN {FS=",";OFS=","}
{if ($5=="EMS: RESPIRATORY EMERGENCY" && $10!="NULL" && $11!="NULL"){arr1[$11]++}}
END{PROCINFO["sorted_in"]="@ind_num_asc"; for (b in arr1) print b, arr1[b], arr1[b]/85  > "respiratory_emergency_calls_by_hour.csv" }
