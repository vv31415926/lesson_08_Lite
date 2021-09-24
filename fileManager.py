import myLibManager
import victory as v
import persAccount as pa
#import os


def goManager():
    goMenu=True
    while goMenu:
        nMenu = myLibManager.menu()

        if nMenu ==   1:
            myLibManager.inNewDir()
        elif nMenu == 2:
            myLibManager.delDir()
        elif nMenu == 3:
            myLibManager.copyFil()
        elif nMenu == 4:
            myLibManager.viewDir()
        elif nMenu == 5:
            myLibManager.viewOnlyDir()
        elif nMenu == 6:
            myLibManager.viewOnlyFil()
        elif nMenu == 7:
            myLibManager.infoOS()
        elif nMenu == 8:
            myLibManager.infoMy()
        elif nMenu == 9:
            v.goGame()
            print('------------------')
        elif nMenu == 10:
            myLibManager.saveDir()
        elif nMenu == 11:
            pa.goGame()
            print('------------------')
        elif nMenu == 12:
            myLibManager.chDir()
            print('------------------')
        elif nMenu == 0:
            goMenu = False
        else:
            print( 'Ошибка выбора!\n-------------')



if __name__ == '__main__':
    #curDir = os.getcwd()   # текущий директорий
    goManager()