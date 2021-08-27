def calculo_recargos(cliente: dict)  -> dict:
    """calculo el procentaje de recargo a aplicar en cada tipo producto"""
   
    umbral_ventas_nacional = 200000000
    umbral_agujas_nacional = 70000000
    umbral_escolares_nacional = 30000000
    umbral_hogar_nacional = 40000000
    
    umbral_ventas_ext = 100000
    umbral_agujas_ext = 25000
    umbral_escolares_ext = 10000
    umbral_hogar_ext = 15000
    
    
    
    
    descuento_menor_umbral = 0
    descuento_mayo_umbral = 0

    nombre =  cliente["nombre"]
    nacional = cliente["nacional"]
    agujas = cliente["agujas"]
    escolares =  cliente["escolares"]
    hogar = cliente["hogar"]

    total_compras =  agujas + escolares + hogar
    if total_compras == 0.0 :
        agujas = 0.0
        escolares= 0.0
        hogar = 0.0
    else:
        if nacional:
            descuento_mayo_umbral = 7.0
            descuento_menor_umbral = 5.0

            if total_compras < umbral_ventas_nacional:
                
                if  agujas > umbral_agujas_nacional and escolares > umbral_escolares_nacional and hogar > umbral_hogar_nacional:
                    agujas = descuento_mayo_umbral
                    escolares = descuento_mayo_umbral
                    hogar = descuento_mayo_umbral
                else:
                    if agujas > umbral_agujas_nacional :
                        agujas = descuento_menor_umbral            
                    else:
                        agujas = 0.0
                    if escolares > umbral_escolares_nacional:
                        escolares = descuento_menor_umbral
                    else:
                        escolares = 0.0    
                    if  hogar > umbral_hogar_nacional :
                        hogar = descuento_menor_umbral
                    else:
                        hogar = 0.0
            else:
                descuento_mayo_umbral = 10.0

                agujas = descuento_mayo_umbral
                escolares = descuento_mayo_umbral
                hogar = descuento_mayo_umbral
                    
        else:
            descuento_mayo_umbral = 5.0
            descuento_menor_umbral = 3.0
            if total_compras < umbral_ventas_ext:
                
                if  agujas > umbral_agujas_ext and escolares > umbral_escolares_ext and hogar > umbral_hogar_ext:
                    agujas = descuento_mayo_umbral
                    escolares = descuento_mayo_umbral
                    hogar = descuento_mayo_umbral
                else:
                    if agujas > umbral_agujas_ext :
                        agujas = descuento_menor_umbral            
                    else:
                        agujas = 0.0 
                    if escolares > umbral_escolares_ext:
                        escolares = descuento_menor_umbral
                    else:
                        escolares = 0.0

                    if  hogar > umbral_hogar_ext :
                        hogar = descuento_menor_umbral
                    else: 
                        hogar = 0.0
            else:
                descuento_mayo_umbral = 8.0

                agujas = descuento_mayo_umbral
                escolares = descuento_mayo_umbral
                hogar = descuento_mayo_umbral
            
    cliente_actulizado  = {
        "nombre" : nombre,
        "agujas" : agujas,
        "escolares" : escolares,
        "hogar" : hogar,

    }
