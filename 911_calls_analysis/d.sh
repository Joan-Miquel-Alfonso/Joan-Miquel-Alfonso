#!/bin/bash
(awk 'BEGIN{
    FS = ","
    print "<HTML><BODY>"
    print "<center><font size=10>Trucades al 911 per Emergència Sanitària al comtat de Montgomery</font></center><br/>"
    print "<font size=4>En aquest primer gràfic mostrarem quantes trucades ha hagut per Emergència Sanitària per hores als dies laborables, per altra banda tenim la mitjana de trucades per dia en cada una de les hores.</font>"
    print "<center><TABLE border=\"1\"></center>"
    print "<TR><TH>HORA</TH><TH>TRUCADES TOTALS</TH><TH>MITJANA DE TRUCADES PER DIA</TH></TR>"
}
{
    printf "<TR>"
    for (i=1; i<=NF; i++) {
        printf "<TD>%s%s%s</TD>", "", $i, ""
    }
    print "</TR>"
}
END {
    print "</TABLE><br/>"
    print "<font size=4>Per tant aquest gràfic ens diu que a les 12 hores és quan normalment hi ha més trucades al 911 mentre que a les 3 hores és quan menys trucades hi ha, per tant podem dir que de 8 a les 20 hores es troben la majoria de trucades.</font><br/><br/>"
    print "</BODY></HTML>"
}' total_calls_by_hour.csv
gnuplot -e 'set terminal canvas; set datafile separator ","; set title "MITJANA DE TRUCADES PER DIA"; plot "total_calls_by_hour.csv" using 1:3 title "mitjana per hora" with lines'
awk 'BEGIN {FS=",";OFS=","} {if ($1>=22 || $1<=5){sum += $2}} END {print "Nit", sum , sum/85, sum/(8*85)} BEGIN {FS=",";OFS=","} {if ($1>=6 && $1<=14){sum1 += $2}} END {print "Matí", sum1 , sum1/85, sum1/(8*85)} BEGIN {FS=",";OFS=","} {if ($1>=15 && $1<=21){sum2 += $2}} END {print "Vesprada", sum2 , sum2/85, sum2/(8*85)} ' total_calls_by_hour.csv | awk 'BEGIN{
    FS = ","
    print "<HTML><BODY>"
    print "<font size=4>En aquest primer gràfic mostrarem quantes trucades ha hagut per Emergència Sanitària per hores als dies laborables, però agrupat per Nit, Matí i vesprada. Els hem agrupat en 8 hores ja que és la jornada laboral.</font>"
    print "<center><TABLE border=\"1\"></center>"
    print "<TR><TH>HORA</TH><TH>TRUCADES TOTALS</TH><TH>MITJANA DE TRUCADES PER DIA</TH><TH>MITJANA DE TRUCADES A CADA HORA</TH></TR>"
}
{
    printf "<TR>"
    for (i=1; i<=NF; i++) {
        printf "<TD>%s%s%s</TD>", "", $i, ""
    }
    print "</TR>"
}
END {
    print "</TABLE><br/>"
    print "<font size=4>Per tant aquest gràfic ens diu que al torn de nit faran falta mínim 5 equips sanitaris, al matí serà quan més siguen necessaris (mínim 11) i per la vesprada mínim hauran de ser 9.</font><br/><br/>"
    print "</BODY></HTML>"
}'
awk 'BEGIN{
    FS = ","
    print "<HTML><BODY>"
    print "<center><font size=10>Trucades al 911 per Emergència Sanitària al comtat de Montgomery per Emergència Respiratòria(Possible COVID)</font></center><br/>"
    print "<font size=4>En aquest primer gràfic mostrarem quantes trucades ha hagut per Emergència Sanitària per hores als dies laborables, les quals fan referència exclusivament a trucades per Emergències respiratòries per altra banda tenim la mitjana de trucades per dia en cada una de les hores per a aquesta variable.</font>"
    print "<TABLE border=\"1\">"
    print "<TR><TH>HORA</TH><TH>TRUCADES TOTALS</TH><TH>MITJANA DE TRUCADES PER DIA</TH></TR>"
}
{
    printf "<TR>"
    for (i=1; i<=NF; i++) {
        printf "<TD>%s%s%s</TD>", "", $i, ""
    }
    print "</TR>"
}
END {
    print "</TABLE><br/>"
    print "<font size=4>Per tant aquest gràfic ens diu que a les 12 és quan normalment hi ha més trucades per Emergència Respirtòria al 911 mentre que a les 4am és quan menys trucades hi ha per aquest mateix motiu.</font><br/><br/>"
    print "</BODY></HTML>"
}' respiratory_emergency_calls_by_hour.csv
awk 'BEGIN {FS=",";OFS=","} {if ($1>=22 || $1<=5){sum += $2}} END {print "Nit", sum , sum/85, sum/(8*85)} BEGIN {FS=",";OFS=","} {if ($1>=6 && $1<=14){sum1 += $2}} END {print "Matí", sum1 , sum1/85, sum1/(8*85)} BEGIN {FS=",";OFS=","} {if ($1>=15 && $1<=21){sum2 += $2}} END {print "Vesprada", sum2 , sum2/85, sum2/(8*85)} ' respiratory_emergency_calls_by_hour.csv | awk 'BEGIN{
    FS = ","
    print "<HTML><BODY>"
    print "<font size=4>En aquest primer gràfic mostrarem quantes trucades ha hagut per Emergència Sanitària per hores als dies laborables quan aquesta emergència ha sigut per emergència respiratòria, però agrupat per Nit, Matí i vesprada. Els hem agrupat en 8 hores ja que és la jornada laboral.</font>"
    print "<center><TABLE border=\"1\"></center>"
    print "<TR><TH>HORA</TH><TH>TRUCADES TOTALS</TH><TH>MITJANA DE TRUCADES PER DIA</TH><TH>MITJANA DE TRUCADES A CADA HORA</TH></TR>"
}
{
    printf "<TR>"
    for (i=1; i<=NF; i++) {
        printf "<TD>%s%s%s</TD>", "", $i, ""
    }
    print "</TR>"
}
END {
    print "</TABLE><br/>"
    print "<font size=4>Per tant aquest gràfic ens diu que al torn de nit faran falta mínim 1 equips sanitaris amb EPIS de nivell 4, al matí serà quan més siguen necessaris (mínim 2) i per la vesprada mínim hauran de ser 1.</font><br/><br/>"
    print "</BODY></HTML>"
}' 
) > 911_report.html

