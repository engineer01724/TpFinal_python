def calcular_precio(cliente_vip, temporada_alta, equipo_nieve, camioneta, cargo_zona, respuesta_dias):

    """
    Calcula el precio total del alquiler del vehículo según condiciones.

    Parámetros:
    
    cliente_vip (bool): Si el cliente tiene descuento VIP.
    temporada_alta (bool): Si el alquiler es en temporada alta.
    equipo_nieve (bool): Si se requiere equipamiento para nieve.
    camioneta (bool): Si el vehículo es una camioneta 4x4.
    cargo_zona (bool): Si se usará en zonas de alto tránsito o turísticas.
    respuesta_dias (int): Cantidad de días de alquiler.

    Retorna:
    total (int): Precio final a pagar."""

    base = 10000
    dia = 100
    if camioneta:
        base += 5000
    if equipo_nieve:
        base += 3000
    if temporada_alta:
        base += 2000
    if cliente_vip:
        base -= 1000
    if cargo_zona:
        base += 2500
    seguro = 2000     
    precio_dias = respuesta_dias * dia
    total = base + precio_dias + seguro
    return total


def imprimir_factura(nombre, dni, tel, domicilio, empresa, tel_lab, vehiculo,
                     cliente_vip, temporada_alta, equipo_nieve, precio_total, patente, numero_chasis, numero_motor, periodo_alquiler):
    """
    Imprime la factura con los datos del cliente y el alquiler del vehículo.

    Parámetros:
    
    nombre, dni, tel, domicilio, empresa, tel_lab (str): Datos personales del cliente.
    vehiculo (str): Tipo de vehículo alquilado.
    cliente_vip, temporada_alta, equipo_nieve (bool): Condiciones aplicadas al alquiler.
    precio_total (int): Monto total a pagar.
    patente, numero_chasis, numero_motor (str): Datos del vehículo.
    periodo_alquiler (str): Duración del alquiler.

    Retorna:
    None
    
    """
     
                     
    print("\n===== FACTURA =====")
    print(f"Cliente: {nombre}")
    print(f"DNI: {dni}")
    print(f"Teléfono: {tel}")
    print(f"Domicilio: {domicilio}")
    print(f"Empresa: {empresa}")
    print(f"Telefono laboral: {tel_lab}")
    print("\n--- Vehículo ---")
    print(f"Tipo: {vehiculo}")
    print(f"Patente: {patente}")
    print(f"N° de chasis: {numero_chasis}")
    print(f"N° de motor: {numero_motor}")
    print(f"VIP: {cliente_vip}")
    print(f"Temporada Alta: {temporada_alta}")
    print(f"Equipo de Nieve: {equipo_nieve}")
    print(f"Periodo de alquiler: {periodo_alquiler}")
    print(f"TOTAL A PAGAR: ${precio_total}")
    print("===================")


def recolectar_datos_usuario():
    """
    Solicita al usuario que ingrese sus datos personales.

    Retorna:
    
    Tuple con: nombre, dni, teléfono, domicilio, empresa, teléfono laboral."""
    nombre = input("Nombre y apellido: ")
    dni = input("DNI: ")
    tel = input("Telefono: ")
    domicilio = input("Domicilio: ")
    empresa = input("Empresa: ")
    tel_lab = input("Teléfono laboral: ")
    return nombre, dni, tel, domicilio, empresa, tel_lab



print("Ingrese su edad")
edad = int(input())
if edad >= 25:
        print("¿Que tipo de licencia posee? ( permiso municipal / nacional / internacional):")
        tipo_licencia = input()
        print("Ingrese el año de vencimiento de la licencia:")
        ano_vencimiento = int(input())

        if tipo_licencia in ["nacional", "internacional", "permiso municipal"] and ano_vencimiento >= 2025:

            print("Licencia válida.")

            print("Durante cuantos dias usara usted el vehiculo? Responda solo con un numero, por favor")
            respuesta_dias = int(input())

            while respuesta_dias <= 0:
                print("Error: La cantidad de días debe ser un número positivo (mayor a 0). Intente nuevamente.")
                respuesta_dias = int(input())

            periodo_alquiler = f"{respuesta_dias} dias"
            if respuesta_dias in [2, 7, 14, 21] or respuesta_dias > 30:
                if respuesta_dias == 2:
                    print("Lo usara durante un fin de semana? (Si, No)")
                    respuesta_finde = input().lower()
                    if respuesta_finde == "si":
                        periodo_alquiler = "Un Fin de Semana"
                elif respuesta_dias in [7, 14, 21]:
                    cant_semanas = respuesta_dias // 7
                    periodo_alquiler = f"Semanal. ({cant_semanas} semanas)"
                elif respuesta_dias > 30:
                    periodo_alquiler = "Mes o superior"
            else:
                periodo_alquiler = f"{respuesta_dias} Dias"

            print("¿Usted es turista nacional, internacional o local?")
            tipo_turista = input()

            nombre, dni, telefono, domicilio, empresa, telefono_laboral = recolectar_datos_usuario()

            print("¿Usted es cliente vip? (si o no)")
            cliente_vip = input().lower() == "si"

            print("¿Usted se va recorrer San carlos de Bariloche? (si o no)")
            zona_bariloche = input().lower() == "si"

            cargo_zona = False
            cargo_tempo_alta = False
            equipo_nieve = False
            camioneta = False

            if zona_bariloche:
                print("¿Usara usted el vehiculo en temporada alta? (Si, No)")
                print("Meses de temporada alta: Junio a Septiembre; Meses de temporada baja: Diciembre a Febrero")
                cargo_tempo_alta = input().lower() == "si"

                print("Usara ud. el vehiculo en las siguietes zonas de alta demanda? (Si, No)")
                print("1- Circuito Chico ")
                print("2- Cerro Catedral")
                print("3- Ruta 40")
                respuesta_zonas = input().lower()
                if respuesta_zonas == "si":
                    cargo_zona = True

                print("¿Usted va a recorrer caminos montañosos y de ripio? (si o no)")
                respuesta_ripio = input().lower()
                if respuesta_ripio == "si":
                    print("Usted va a recorrer caminos montañosos y de ripio. Se le asigna una 4x4 obligatoriamente")
                    camioneta = True
                    vehiculo = "Camioneta 4x4"
                    patente = "AC978ED"
                    numero_chasis = "CHS-8372-XT91"
                    numero_motor = "MTR-50218"
                else:
                    print("¿Que tipo de vehículo desea usar en Bariloche? (auto o 4x4)")
                    eleccion = input().lower()
                    if eleccion == "4x4":
                        camioneta = True
                        vehiculo = "Camioneta 4x4"
                        patente = "AC978ED"
                        numero_chasis = "CHS-8372-XT91"
                        numero_motor = "MTR-50218"
                    else:
                        vehiculo = "Auto"
                        patente = "AB977KL"
                        numero_chasis = "CKP-0932-HJ90"
                        numero_motor = "MOP-67800"

                print("¿Necesita equipo para nieve? (si o no)")
                equipo_nieve = input().lower() == "si"

            else:
                print("¿Que tipo de vehiculo desea alquilar? (4x4 o auto)")
                vehiculo = input().lower()
                if vehiculo == "4x4":
                    camioneta = True
                    patente = "AC978ED"
                    numero_chasis = "CHS-8372-XT91"
                    numero_motor = "MTR-50218"
                else:
                    camioneta = False
                    vehiculo = "Auto"
                    patente = "AB977KL"
                    numero_chasis = "CKP-0932-HJ90"
                    numero_motor = "MOP-67800"

                print("¿Necesita equipo para nieve? (si o no)")
                equipo_nieve = input().lower() == "si"

            precio_total = calcular_precio(cliente_vip, cargo_tempo_alta, equipo_nieve, camioneta, cargo_zona, respuesta_dias)

            imprimir_factura(nombre, dni, telefono, domicilio, empresa, telefono_laboral,
                             vehiculo, cliente_vip, cargo_tempo_alta, equipo_nieve, precio_total,
                             patente, numero_chasis, numero_motor, periodo_alquiler)

            
            print("¿Desea pagar el monto total o un pago parcial? (total/parcial)")
            opcion_pago = input().lower()
            if opcion_pago == "total":
                print(f"Pago total de ${precio_total} recibido. ")
            elif opcion_pago == "parcial":
                valid = False
                while valid == False:
                    print(f"El total a pagar es ${precio_total}. ¿Cuanto desea pagar ahora?")
                    pago_parcial = float(input())
                    if pago_parcial > precio_total or pago_parcial <= 0:
                        print("El pago parcial no puede ser mayor al total o igual / menor a 0. Intente nuevamente.")
                    else:
                        saldo = precio_total - pago_parcial
                        print(f"Pago parcial recibido por ${pago_parcial}.")
                        print(f"Saldo restante por pagar: ${saldo}")
                        
                        valid = True
            else:
                print("Opción de pago no valida. Por favor reinicie el proceso y elija 'total' o 'parcial'.")

        else:
            print("Licencia no valida o vencida.")
            
else:
    print("Edad insuficiente para alquilar un vehiculo.")
