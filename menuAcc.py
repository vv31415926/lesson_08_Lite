import myLibAcc

def goGame( history ):
    persAcc = myLibAcc.getAccount( history )

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            # пополнение счета
            s = float(  input( 'Введите сумму пополнения счёта (руб):')  )
            persAcc, _ = myLibAcc.setAccount( persAcc, s )
            history = myLibAcc.setHistory( 'Пополнение', s, persAcc, history, 'одобрено')
            print()

        elif choice == '2':
            p = input(  'Введите, что покупаете:'  )
            t = float(   input(  'Введите сумму покупки (руб):' )   )
            persAcc, isOK = myLibAcc.setAccount( persAcc, t, input = False )
            if not isOK:
                print(  'На счету мало средств!\n')
                history = myLibAcc.setHistory( p, t, persAcc, history, 'отказ')
            else:
                history = myLibAcc.setHistory( p, t, persAcc, history, 'одобрено')
            print()

        elif choice == '3':
            print( 'История покупок: ')
            lst = myLibAcc.list_history( history )
            for v in lst:
                print(  v )
            print( '------\n')
        elif choice == '4':
            myLibAcc.write_history( history )
            break
        else:
            print('Неверный пункт меню')