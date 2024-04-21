from time import sleep
import mysql.connector

conexao = mysql.connector.connect (
    host='localhost',
    user='root',
    password = '',
    database = 'db_stats_football_py',
)

cursor = conexao.cursor()

def exit(): 
    print('Ok, saindo...')
    sleep(2)
    print('Programa encerrado!')

def statsFootballUX():
    while True: 
        var_choice = str(input('Deseja utilizar o Stats Football Py [S/N]: '))

        if var_choice.upper() == 'S': 
            var_choice = str(input('Deseja inserir ou mostrar os valores [inserir/mostrar]: '))

            if var_choice.upper() == 'INSERIR': 
                try: 
                    while True: 
                        var_nome = str(input('Digite o nome do jogador: '))
                        var_gols = int(input('Digite o número de gols: '))
                        var_assis = int(input('Digite o número de assistências: '))
                        var_partida = int(input('Digite o número de partidas: '))
                        media_gols = var_gols / var_partida
                        media_assis = var_assis / var_partida

                        comando = f'INSERT INTO jogadores_stats(nome_jogador, gols, assistencias, partidas, media_gols_partida, media_assistencias_partida) VALUES ("{var_nome}", {var_gols}, {var_assis}, {var_partida}, {media_gols}, {media_assis})'
                        cursor.execute(comando)
                        conexao.commit()

                        var_choice = str(input('Deseja continuar? [S/N]: '))

                        if var_choice.upper() == 'N': 
                            break
                    var_choice = str(input('Deseja mostrar os valores? [S/N]: '))
                    try: 
                        if var_choice.upper() == 'S': 
                            comando_sel = 'SELECT * FROM jogadores_stats'
                            cursor.execute(comando_sel)
                            resultado_sel = cursor.fetchall()

                            print(f'{"ID":<5} {"NOME":<25} {"GOLS":<10} {"ASSISTÊNCIAS":<14} {"PARTIDAS":<8} {"MÉDIA DE GOLS P/ PARTIDA":<25} {"MÉDIA DE ASSISTÊNCIAS P/ PARTIDA":<30}')
                            print('='*100)
                            for x in resultado_sel:
                                print(f'{x[0]:<5} {x[1]:<25} {x[2]:<10} {x[3]:<12} {x[4]:<8} {x[5]:<25} {x[6]:<30}')
                        elif var_choice.upper() == 'N': 
                            exit()
                            break
                    except TypeError: 
                        print(f'Error: tipo de valor inválido!')
                except TypeError: 
                    print(f'Error: tipo de valor inválido!')
            elif var_choice.upper() == 'MOSTRAR': 
                try: 
                    comando_sel = 'SELECT * FROM jogadores_stats'
                    cursor.execute(comando_sel)
                    resultado_sel = cursor.fetchall()

                    print(f'{"ID":<5} {"NOME":<25} {"GOLS":<10} {"ASSISTÊNCIAS":<14} {"PARTIDAS":<8} {"MÉDIA DE GOLS P/ PARTIDA":<25} {"MÉDIA DE ASSISTÊNCIAS P/ PARTIDA":<30}')
                    print('='*100)
                    for x in resultado_sel:
                        print(f'{x[0]:<5} {x[1]:<25} {x[2]:<10} {x[3]:<12} {x[4]:<8} {x[5]:<25} {x[6]:<30}')
                except ValueError: 
                    print(f'Error: valor escolhido inválido!')
        elif var_choice.upper() == 'N': 
            exit()
            break

if __name__ == '__main__': 
    statsFootballUX()
