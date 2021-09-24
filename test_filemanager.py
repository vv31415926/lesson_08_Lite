'''
0. В проекте ""Консольный файловый менеджер"" перейти на новую ветку для добавления нового функционала;
1. Где это возможно переписать код с использованием генераторов и тернарных операторов;
2. Там где возможны исключительные ситуации добавить обработку исключений;
3. *Где это возможно применить декораторы.
Иногда может быть так, что применить новые возможности негде, особенно декораторы - это нормально.
ДОПОЛНИТЕЛЬНО:
Написать тесты для всех новых функций в проекте.
4. Создать pull request на объединение веток master и новой ветки, прислать ссылку на pull request как решение дз"
'''
import victory
from myLibManager import *

def test_victory_Day():

    assert victory.getDay('01')  == 'первое'
    assert victory.getDay('10') == 'десятое'
    assert victory.getDay('12') == 'двенадцатое'
    assert victory.getDay('20') == 'двадцатое'
    assert victory.getDay('25') == 'двадцать пятое'
    assert victory.getDay('30') == 'тридцатое'
    assert victory.getDay('31') == 'тридцать первое'

def test_victory_Month():
    assert victory.getMonth('01') == 'января'
    assert victory.getMonth('12') == 'декабря'

def test_victory_bDayOut():
    assert victory.bDayOut( '01.01.2012') == 'первое января 2012 года'

def test_victory_errDay():
    assert not victory.getDay('hiuh')

def test_victory_errMonth():
    assert not victory.getMonth('hiuh')

import os
def test_newDir():
    d = 'mytestnewdir'
    if d in os.listdir():
        os.rmdir( d )
    assert newDir( d ) == True
    if d in os.listdir():
        os.rmdir( d )