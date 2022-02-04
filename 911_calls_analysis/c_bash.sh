#!/bin/bash
OLDIFS=$IFS
IFS=','
[ ! -f "911_2020_march-june_EMS.csv" ] && { echo "911_2020_march-june_EMS.csv file not found"; exit 99; }
while read lat lng desc zip title timeStamp twp addr e hour1 hour2
do
if [ "$e" == "e" ];
then
echo $lat,$lng,$desc,$zip,$title,$timeStamp,$twp,$addr,$e,$hour1,$hour2,"Corregit"
elif [ -z "$hour1" ] &&  [  "$hour2" -eq "$hour2" ] 2>/dev/null;
then
echo $lat,$lng,$desc,$zip,$title,$timeStamp,$twp,$addr,$e,$hour2,$hour2,"Sí"
elif [ -z "$hour2" ] && [  "$hour1" -eq "$hour1" ] 2>/dev/null;
then
echo $lat,$lng,$desc,$zip,$title,$timeStamp,$twp,$addr,$e,$hour1,$hour1,"Sí"
elif [ -z "$hour1" ] && [ -z "$hour2" ];
then
echo $lat,$lng,$desc,$zip,$title,$timeStamp,$twp,$addr,$e,"NULL","NULL","Sí"
elif ! [  "$hour1" -eq "$hour1" ] 2>/dev/null && ! [  "$hour2" -eq "$hour2" ] 2>/dev/null;
then
echo $lat,$lng,$desc,$zip,$title,$timeStamp,$twp,$addr,$e,"NULL","NULL","Sí"
elif ! [  "$hour1" -eq "$hour1" ] 2>/dev/null;
then
echo $lat,$lng,$desc,$zip,$title,$timeStamp,$twp,$addr,$e,$hour2,$hour2,"Sí"
elif ! [  "$hour2" -eq "$hour2" ] 2>/dev/null; 
then
echo $lat,$lng,$desc,$zip,$title,$timeStamp,$twp,$addr,$e,$hour1,$hour1,"Sí" 
elif (( $(echo "$hour1==$hour2" | bc) ));
then
echo $lat,$lng,$desc,$zip,$title,$timeStamp,$twp,$addr,$e,$hour1,$hour2,"No"
elif (( $(echo "$hour1!=$hour2" | bc) ));
then
echo $lat,$lng,$desc,$zip,$title,$timeStamp,$twp,$addr,$e,$(echo "($hour1+$hour2)/2" | bc),$(echo "($hour1+$hour2)/2" | bc),"Sí"
fi
done < 911_2020_march-june_EMS.csv
IFS=$OLDIFS
