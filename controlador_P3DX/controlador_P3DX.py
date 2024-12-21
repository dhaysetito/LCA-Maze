'''Você instalou o Matlplt e o networkx no Local'''

from controller import Robot
import networkx as nx
import numpy as np



MAZE = np.array([[0,0,0],
                 [0,0,0],
                 [0,0,0]])

position = [2 ,2 ,'E']

def set_speed(left, right):
    left_motor.setVelocity(left)
    right_motor.setVelocity(right)

def move_forward():
    set_speed(1.2, 1.2)
    robot.step(timestep)
    set_speed(0, 0)

def turn_left():
    set_speed(-1.2, 1.2)
    robot.step(timestep)
    set_speed(0, 0)

def turn_right():
    set_speed(1.2, -1.2)
    robot.step(timestep)
    set_speed(0, 0)
 
def rotate(angle):

    angular_speed = 0.5908 
    angle_rad = np.radians(angle)  # Converte o ângulo para radianos

    # Tempo necessário para girar o ângulo desejado
    rotation_time = abs(angle_rad) / angular_speed

    # Configura a direção do giro
    if angle > 0:  # Sentido anti-horário
        set_speed(-1, 1)
    else:  # Sentido horário
        set_speed(1, -1)

    # Executa o giro pelo tempo necessário
    start_time = robot.getTime()
    while robot.getTime() - start_time < rotation_time:
        robot.step(timestep)

    # Para os motores após o giro
    set_speed(0, 0)

def probe_direction():
    """Lê as medidas dos sensores."""
    robot.step(timestep)
    distances = []
    for sensor in sensores:
        distance = float('{:.1f}'.format(sensor.getValue()))
        distances.append(distance)
    return distances

def probe_for_walls():
    """
    Analisa as paredes ao redor do robô e retorna uma lista indicando a presença de paredes
    em relação às direções absolutas do labirinto [N, E, S, W].
    """
    directions = ['N', 'E', 'S', 'W']  # Ordem fixa das direções absolutas
    wall_detection = [0, 0, 0, 0]  # Inicializar detecção de paredes

    # Identificar o índice da direção atual no labirinto
    current_dir_index = directions.index(position[2])

    for _ in range(4):
        # Capturar leituras dos sensores
        probe = probe_direction()

        # Determinar se há uma parede à frente (critério ajustável conforme o sensor)
        if probe[3] > 940 and probe[4] > 940:
            wall_detection[current_dir_index] = 1  # Parede detectada

        # Atualizar a direção atual
        current_dir_index = (current_dir_index + 1) % 4
        
        # Rotacionar o robô 90 graus para a próxima direção
        rotate(-90)
    
    # Retornar à orientação original
    rotate(-90 * (current_dir_index - directions.index(position[2])) + 2.3)  #2 é o erro
    return wall_detection

def move_on_edge(direction, maze=MAZE):
    """
    Move o robô 2 metros na direção especificada (N, S, E ou W).
    No final da execução o robo apontara para a direção de movimento
    """
    directions = ['N', 'E', 'S', 'W']
    current_dir_index = directions.index(direction) # direção de movimento desejada
    translation_time = 10.26227291 # Tempo necessário para percorrer 2 metros (distanciaDeUmPasso_emmetros/velocidade_linear)

    rotate(-90 * (current_dir_index - directions.index(position[2])))
    position[2] = direction

    #atualiza a posição do robô
    if direction == 'N':
        position[0] -= 1
    elif direction == 'E':
        position[1] += 1
    elif direction == 'S':
        position[0] += 1
    elif direction == 'W':
        position[1] -= 1
    
    # Movimentar para frente
    start_time = robot.getTime()
    set_speed(1, 1)  # Velocidade constante
    while robot.getTime() - start_time < translation_time:
        robot.step(timestep)

    # Parar o robô
    set_speed(0, 0)

    #situações de borda
    limit_directions = [0, 0, 0, 0]
    limit = True
    #testar se existem limites em alguma direção
    try:
        if maze[position[0]+1, position[1]] == 0 or 1:
            pass
    except IndexError:
        limit = False
        limit_directions[0] = 1
    try:
        if maze[position[0], position[1]+1] == 0 or 1:
            pass
    except IndexError:
        limit = False
        limit_directions[1] = 1
    try:
        if maze[position[0]-1, position[1]] == 0 or 1:
            pass
    except IndexError:
        limit = False
        limit_directions[2] = 1
    try:
        if maze[position[0], position[1]-1] == 0 or 1:
            pass
    except IndexError:
        limit = False
        limit_directions[3] = 1
       
    #adicionar novos limites caso não existam
    if limit == False:
        for i in range(4):
            if limit_directions[i] == 1:
                if directions[i] == 'N':
                    maze = np.vstack((np.zeros(maze.shape[1]), maze))
                elif directions[i] == 'E':
                    maze = np.hstack((maze, np.zeros((maze.shape[0], 1))))
                elif directions[i] == 'S':
                    maze = np.vstack((maze, np.zeros(maze.shape[1])))
                elif directions[i] == 'W':
                    maze = np.hstack((np.zeros((maze.shape[0], 1)), maze))
    
    global MAZE
    MAZE = maze

# Configurações iniciais do robô --------------------------------------------------------x
robot = Robot()
timestep = int(robot.getBasicTimeStep())   

# Inicializar motores e sensores
left_motor = robot.getDevice('left wheel')
right_motor = robot.getDevice('right wheel')
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0)
right_motor.setVelocity(0)

so0 = robot.getDevice('so0')
so1 = robot.getDevice('so1')
so2 = robot.getDevice('so2')
so3 = robot.getDevice('so3')
so4 = robot.getDevice('so3')
so5 = robot.getDevice('so5')
so6 = robot.getDevice('so6')
so7 = robot.getDevice('so7')
sensores = [so0, so1, so2, so3, so4, so5, so6, so7]
for sensor in sensores:
    sensor.enable(timestep)


move_on_edge('S')
move_on_edge('S')
move_on_edge('W');move_on_edge('W')
move_on_edge('N')
move_on_edge('E')
print(probe_for_walls())
print(MAZE)
print(position)
move_on_edge('W')
move_on_edge('S')
move_on_edge('E');move_on_edge('E')
move_on_edge('N');move_on_edge('N')
print(probe_for_walls())
print(MAZE)
print(position)
move_on_edge('E')
move_on_edge('S');move_on_edge('S')
move_on_edge('E');move_on_edge('E')
move_on_edge('S')
print(probe_for_walls())
print(MAZE)
print(position)
move_on_edge('N')
move_on_edge('W');move_on_edge('W')
move_on_edge('N');move_on_edge('N')
move_on_edge('W')
print(probe_for_walls())
print(MAZE)
print(position)


