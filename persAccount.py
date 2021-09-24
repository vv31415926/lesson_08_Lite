import menuAcc
import myLibAcc

def goGame():
    history = myLibAcc.read_history()
    menuAcc.goGame(history)

if __name__ == '__main__':
    goGame()
