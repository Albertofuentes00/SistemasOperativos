script=""
while true
do
    echo "MENU"
    echo "1.Holamundo"
    echo "2.Holamundo_variables"
    echo "3.Variables"
    echo "4.Arrays"
    echo "5.Valor_variable"
    echo "6.Operaciones_artimeticas"
    echo "7.Operaciones_logicas"
    echo "8.Condicionales_ifytest"
    echo "9.Condicionales_combinaciones"
    echo "10.Condicionales_Friky"
    echo "11.Iteraciones_for"
    echo "12.Iteraciones_while"
    echo "13.Iteracion_until"
    echo "14.Iteracion_select"
    echo "15.Funciones"
    echo "16.Librerias"
    echo "17.Señales"
    echo "18.Colores"
    echo "19.Salir"
    echo "Escoge una opcion"
    read script
    case $script in
        1)
            source holamundo.sh
        ;;
        2)
            source holamundovariable.sh
        ;;
        3)
            source variables.sh
        ;;
        4)
            source Arrays.sh
        ;;
        5)
            source valorvariable.sh
        ;;
        6)
            source Aritmeticas.sh
        ;;
        7)
            source Logicas.sh
        ;;
        8)
            source If.sh
        ;;
        9)
            source combinaciones.sh
        ;;
        10)
            source Friky.sh
        ;;
        11)
            source For.sh
        ;;
        12)
            source while.sh
        ;;
        13)
            source Iteracion.sh
        ;;
        14)
            source select.sh
        ;;
        15)
            source funciones.sh
        ;;
        16)
            source anteriores.sh
        ;;
        17)
            source señales.sh
        ;;
        18)
            source colores.sh
        ;;
        19)
            break
        ;;
        *)
            echo "Escoge una opcion"
        ;;
    esac
done
