import random

#Función para escoger opciones del juego para la computadora, como pra el usuario.
def chose_options():
  options = ('Piedra','Papel','Tijera')
  user_option = input('Elige y escribe una Piedra, Papel, Tijera =>')
  user_option = user_option.capitalize()

  
  if not user_option in options:
    print('Esa opción no es valida')
    # continue
    return None, None
  computes_option = random.choice(options)
  computes_option = computes_option.capitalize()
  
  print('Player => ', user_option)
  print('Computer => ',computes_option)
  return(user_option, computes_option)
  
# Funcion que verifica las reglas del Juego 
def check_rules(user_option, computes_option, user_wins, computer_wins):
  
  if user_option == computes_option :
      print("Empate!! ")
  elif user_option == "Piedra":
    if computes_option == "Tijera":
      print('Piedra gana a Tijera')
      print('User Gana!!')
      user_wins += 1
    else:
      print('Papel gana a Piedra')
      print('Computer Gana!!')
      computer_wins += 1
      
  elif user_option == 'Papel':
    if computes_option == 'Piedra':
      print('Papel gana a Piedra')
      print('User Gana!!')
      user_wins += 1
      
    else:
      print('Tijera gana a Papel')
      print('Computer Gana!!')
      computer_wins += 1
      
  elif user_option == 'Tijera':
    if computes_option == 'Papel':
      print('Tijera gana a Papel')
      print('User Gana!!')
      user_wins += 1
      
    else:
      print('Piedra gana a Tijera')
      print('Computer Gana!!')
      computer_wins += 1
  return user_wins, computer_wins
    
#Funcionque principal del juego, función que 
def run_game():
   rounds = 1
   computer_wins =0
   user_wins = 0
   while True:
    print('*'*10)
    print('ROUND',rounds)
    print('*'*10)
  
    print('Compureter Wins ', computer_wins)
    print('User Wins ', user_wins)
    rounds += 1
    
    user_option, computes_option = chose_options()
    user_wins, computer_wins = check_rules (user_option, computes_option, user_wins, computer_wins)

    if computer_wins == 2:
     print("El rotundo ganador es la computadora")
     break
    if user_wins == 2:
      print("El rotundo ganador es el usuario")
      break
  
run_game()