from flask import Flask, render_template, request
from stockfish import Stockfish
s = Stockfish("bin/stockfish")
s.set_position(["e2e4", "e7e6"])
#stockfish.get_board_visual()
#s.get_board_visual()
print(s.get_best_move())


app = Flask(__name__)

@app.route("/<user>/<move>")
def my_form(user,move):
    print("User Name :", user)
    print("Move :", move)
if __name__=="__main__":
    app.run()
