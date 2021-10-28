def invalido():
    print("digite um numero valido")

def venda():
    print(f'Pedido= {sabor} {ml} com {gelo}, em {copo} e {tipo_copo}')


while True:
    bebida = input('selecione o tipo de bebida, Suco(0) Refrigerante(1):\n')
    if bebida.isdigit():
        bebida = int(bebida)

    if bebida == 1:
        copo = 'copo de papel'

        refrigerante = input('Coca-Cola(0) Guarana(1):\n')
        if refrigerante.isdigit():
            refrigerante = int(refrigerante)

        if refrigerante == 0:
            sabor = 'Coca-Cola'

        elif refrigerante == 1:
            sabor = 'Guarana'

        else:
            invalido()
            continue

        tamanhoRefri = input('Selecione o tamanho da bebida: 300ml(0), 500ml(1), 700ml(2):\n')
        if tamanhoRefri.isdigit():
            tamanhoRefri = int(tamanhoRefri)

        if tamanhoRefri == 0:
            ml = '300ml'

        elif tamanhoRefri == 1:
            ml = '500ml'

        elif tamanhoRefri == 2:
            ml = '700ml'

        else:
            invalido()
            continue

        geloRefri = input('Gelo na bebida? (0)SIM ou (1)NÃO:\n')
        if geloRefri.isdigit():
            geloRefri = int(geloRefri)

        if geloRefri == 0:
            gelo = '6 cubos de gelo'

        elif geloRefri == 1:
            gelo = 'nenhum cubo de gelo'

        else:
            invalido()
            continue

        entrega = input("(0)LOCAL ou (1)DELIVERY:\n")
        if entrega.isdigit():
            entrega = int(entrega)

        if entrega == 0:
            tipo_copo = 'uma tampa com furo para canudo'

        elif entrega == 1:
            tipo_copo = 'uma tampa sem furo para canudo'

        else:
            invalido()
            continue

        venda()
        print()
        pedido = input('O pedido está correto? (0)SIM ou (1)NÃO\n')

        if pedido.isdigit():
            pedido = int(pedido)
        if pedido == 0:
            print('Pedido Enviado')
            repetição = input('Gostaria de realizar outro pedido? (0)SIM (1)NÃO\n')
            if repetição.isdigit():
                repetição = int(repetição)

            if repetição == 0:
                continue
            elif repetição == 1:
                print('Obrigado por comprar conosco')
                break
            else:
                invalido()
                continue
        elif pedido == 1:
            print('Por favor, refaça o seu pedido.')
            continue
        else:
            invalido()
            continue

    elif bebida == 0:
        copo = 'copo de plastico'

        suco = input('Uva(0) Laranja(1):\n')
        if suco.isdigit():
            suco = int(suco)
        if suco == 0:
            sabor = 'Suco de uva'

        elif suco == 1:
            sabor = 'Suco de laranja'

        else:
            invalido()
            continue

        tamanhoSuco = input('Selecione o tamanho da bebida: 300ml(0), 500ml(1):\n')
        if tamanhoSuco.isdigit():
            tamanhoSuco = int(tamanhoSuco)
        if tamanhoSuco == 0:
            ml = '300ml'

        elif tamanhoSuco == 1:
            ml = '500ml'

        else:
            invalido()
            continue

        cubos_gelo = input('Gelo na bebida? (0)SIM ou (1)NÃO:\n')
        if cubos_gelo.isdigit():
            cubos_gelo = int(cubos_gelo)
        if cubos_gelo == 0:
            gelo = '12 cubos de gelo'

        elif cubos_gelo == 1:
            gelo = 'nenhum cubo de gelo'

        else:
            invalido()
            continue
        entregaSuco = input('(0)LOCAL (1)DELIVERY\n')
        if entregaSuco.isdigit():
            entregaSuco= int(entregaSuco)

        if entregaSuco == 0:
            tipo_copo = 'uma tampa com furo para canudo'

        elif entregaSuco == 1:
            tipo_copo = 'uma tampa sem furo para canudo'

        else:
            invalido()
            continue

        venda()
        print()
        pedido = input('O pedido está correto? (0)SIM ou (1)NÃO\n')

        if pedido.isdigit():
            pedido = int(pedido)
        if pedido == 0:
            print('Pedido Enviado')
            repetição = input('Gostaria de realizar outro pedido? (0)SIM (1)NÃO\n')
            if repetição.isdigit():
                repetição = int(repetição)

            if repetição == 0:
                continue
            elif repetição == 1:
                print('Obrigado por comprar conosco')
                break
            else:
                invalido()
                continue
        elif pedido == 1:
            print('Por favor, refaça o seu pedido.')
            continue
        else:
            invalido()
            continue

    else:
        invalido()
        continue