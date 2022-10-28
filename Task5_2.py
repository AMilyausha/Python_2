# Создайте программу для игры в ""Крестики-нолики"".
board = list(range(1,10))
# Рисуем доску
def draw_board(board):
   print("-------------")
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-------------")
# Сделать ход 
def step_input(step):
   while True:
      player_answer = int(input("Куда поставим " + step+"? "))
      if player_answer >= 1 and player_answer <= 9:
         if(str(board[player_answer-1]) not in "XO"):
            board[player_answer-1] = step
            return True
         else:
            print("Эта клетка уже занята!")
# Инициализация победы
def check_win(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False
# Основная функция игры
def main(board):
    counter = 0
    while True:
        draw_board(board)
        if counter % 2 == 0:
           step_input("X")
        else:
           step_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win(board)
           if tmp:
              print(tmp, "выиграл!")
              return True
              break
        if counter == 9:
            print("Ничья!")
            break
main(board)
