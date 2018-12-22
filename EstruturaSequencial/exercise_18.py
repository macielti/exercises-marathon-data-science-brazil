'''18. Faça um programa que peça o tamanho de um arquivo para download 
(em MB) e a velocidade de um link de Internet (em Mbps), calcule e 
informe o tempo aproximado de download do arquivo usando este link 
(em minutos).'''

tamanho_arquivo = float(input('Tamanho do arquivo em MBs: '))
velocidade_em_mbps = float(input('Velocidade em Mbps: '))

minutos  = (tamanho_arquivo / velocidade_em_mbps) / 60

print('Tempo de downloads em minutos:', minutos, 'min')
