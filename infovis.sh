case "$1" in 
    start)
	echo "=========================================Starting Infovis Server============================================"
	nohup python manage.py runserver 0.0.0.0:8000 &
	LASTPID=$!
	echo $LASTPID > translate.pid
    ;;
    stop)
	echo "=========================================Stoping Infovis Server============================================"
	$INFOVISPID=$(cat /home/ubuntu/infovis/translate.pid)
	echo $INFOVISPID
	pkill -9 -P $INFOVISPID
    ;;
esac
exit 0
