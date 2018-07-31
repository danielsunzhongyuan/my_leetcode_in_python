# Read from the file file.txt and output the tenth line to stdout.
# cat file.txt | sed -n 10p
# sed -n 10p file.txt
# awk '{ if (FNR==10) print $0 }' file.txt

line_count=1
pivot=10
while read name
do
    if [ "$line_count" -eq "$pivot" ]
    then
        echo $name
    fi
    line_count=`expr $line_count + 1`
done < "file.txt"
if [ "$pivot" -ge "$line_count" ]
then
    echo ""
fi

