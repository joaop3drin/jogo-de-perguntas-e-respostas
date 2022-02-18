perguntas = {
    'pergunta 1':{
        'pergunta':'Quanto é 1+1?',
        'respostas' : { 'a':'1','b':'2', 'c':'3', 'd':'4'},
        'resposta certa': 'b',
    },
        'pergunta 2':{
        'pergunta':'Quanto é 1-1?',
        'respostas' : {' a ' : '1' ,  ' b ' : '2',  'c' : '0',  'd' : ' 4' },
        'resposta certa': 'c',
    },
        'pergunta 3':{
        'pergunta':'Quanto é 1*1?',
        'respostas' : {  'a' : '1', 'b' : '2', 'c ' : '3',  'd' : '4' },
        'resposta certa': 'a',
    }
}

respostas_certas = 0
for pk, pv in  perguntas.items():
    print(f' {pk}: {pv["pergunta"]}')

    for rk, rv in pv['respostas'].items():
        print(f'{rk}) {rv}')

        respostau = input('digite sua resposta: ')
        print()

