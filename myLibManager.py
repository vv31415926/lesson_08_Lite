import os
import shutil
import platform


def menu():
    print('1  создать папку                                  ',
          '2  удалить (файл/папку)      ',
          '3  копировать (файл/папку)  \n',
          '4  просмотр содержимого рабочей директории        ',
          '5  посмотреть только папки   ',
          '6  посмотреть только файлы  \n',
          '7  просмотр информации об операционной системе    ',
          '8  создатель программы       ',
          '9  играть в викторину       \n',
          '10 сохранить содержимое рабочей директории в файл ',
          '11 мой банковский счет       ',
          '12 смена рабочей директории \n',
          '0  выход                                        \n', sep='')
    while True:
        n = input('Введите номер пункта меню: ')
        if not n.isdigit():
            print('Ошибка выбора.')
        else:
            break
    return int(n)
# ------------------------------------------------------


def outSeparator( f ):
    def wrapper(*args, **kwargs):
        print('----------------')
        rez = f(*args, **kwargs)
        print('----------------\n')
        return rez
    return wrapper


@outSeparator
def inNewDir():
    s = input(  'Введите имя новой папки: ')
    if not os.path.exists(s):
        if not newDir( s ):
            print( 'Папка не создана.')
    else:
        print( 'такой файл/папка уже есть')


def newDir( name ):
    os.mkdir( name )
    if name in os.listdir():
        return True
    else:
        return False
# ------------------------------------------------------

@outSeparator
def delDir( ):
    s = input(  'Введите имя папки для удаления: ')
    p = os.path.join( os.getcwd(), s )
    if os.path.exists( p ):
        os.rmdir( p )
    else:
        print( 'нет файла/папки: '+p )
    return p
# ----------------------------------------------------


@outSeparator
def copyFil():
    srcF = input('Введите имя файла для копирования: ')
    n = 1
    while n == 1:
        if not os.path.exists( srcF ):
            n = int(  input( 'Нет такого файла. \nОтмена: 0 \nПовтор: 1 \nввести:')   )
        else:
            n = 2
    dstF = input('Введите путь\имя файла куда копировать: ')
    n = 1
    while n == 1:
        if not os.path.exists(dstF):
            n = int(input('Нет такого пути. \nОтмена: 0 \nПовтор: 1 \nввести:'))
        else:
            n = 2
    if n == 2:
        shutil.copy( srcF, dstF )
# ------------------------------------------------------


@outSeparator
def viewDir():
    lst = os.listdir( os.getcwd() )
    print( lst )
# ------------------------------------------------------


@outSeparator
def saveDir():
    lst = os.listdir(os.getcwd())
    lst_dir=[]
    lst_file=[]
    with open( 'listdir.txt', 'w' ) as f:
        for s in lst:
            if os.path.isfile( s ):
                lst_file.append( s )
            else:
                lst_dir.append( s )
        f.write( 'files: ' )
        f.write( ','.join( lst_file )  )
        f.write('\n')

        f.write('dirs: ')
        f.write(','.join(lst_dir))

        print( 'Сохранено в listdir.txt:\n','files: ',lst_file)
        print( 'dirs: ',lst_dir)
# -------------------------------------------------------


@outSeparator
def viewOnlyDir():
    lst = os.listdir( os.getcwd() )
    lst = list(   filter(  lambda x: os.path.isdir(x), lst )    )
    print( lst )
# ------------------------------------------------------


@outSeparator
def viewOnlyFil():
    lst = os.listdir( os.getcwd() )
    lst = list(   filter(  lambda x: os.path.isfile(x), lst )    )
    print( lst )
# ------------------------------------------------------


@outSeparator
def infoOS():
    print(  platform.uname() )
# ------------------------------------------------------


@outSeparator
def infoMy():
    print(  'Создатель - Василич' )
# ------------------------------------------------------

@outSeparator
def chDir():
    n = 1
    while n == 1:
        src = input('Введите путь на новую директорию: ')
        if not os.path.isabs(src):
            src = os.path.abspath(src)

        if not os.path.exists( src ):
            n = int(  input( 'Нет такой директории. \nОтмена: 0 \nПовтор: 1 \nввести:')   )
        else:
            if not os.path.isfile( src ):
                n = 2
            else:
                n = int(input('Вы ввели файл. \nОтмена: 0 \nПовтор: 1 \nввести:'))

    if n == 2:
        os.chdir( src )
        print( 'Текущий рабочий каталог: ', os.getcwd() )
