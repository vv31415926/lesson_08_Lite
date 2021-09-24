import myLibAcc

def test_setAccount():
    assert myLibAcc.setAccount(  0, 10, input=True ) == (10,True )
    assert myLibAcc.setAccount( 10,  5, input=False) == ( 5,True )
    assert myLibAcc.setAccount(  5, 10, input=False) == ( 5,False)