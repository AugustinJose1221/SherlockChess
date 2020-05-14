from stockfish import Stockfish
s = Stockfish("bin/stockfish")
s.set_position(["e2e4", "e7e6"])
#stockfish.get_board_visual()
#s.get_board_visual()
print(s.get_best_move())
print(s)
