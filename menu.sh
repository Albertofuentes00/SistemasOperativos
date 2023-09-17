script=""
while true
do
echo -e "\033[40m\033[37m ~ M e n u ~ \033[0m"
echo "		"
echo -e "\033[40m\033[1;33m 1. Script Arbol de directorios \033[0m"
echo -e "\033[40m\033[1;33m 2. Script Hola mundo \033[0m"
echo -e "\033[40m\033[1;33m 3. Script Saludo con variables \033[0m"
echo -e "\033[40m\033[31m x. Salir \033[0m"
echo "		"
echo -n "Elige una opcion"
read script 
case ${script} in 

	1) 
		source arbol.sh
		;;

	2)
		source holamundo.sh
		;;

	3) 
		source saludo.sh
		;;

	x) 
		break
		;;

	*)
		echo "ELIGE UNA OPCION DE ARRIBA >:C"
esac
done 

