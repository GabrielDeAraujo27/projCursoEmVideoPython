def tNotas(r='s'):
    notas = {"maiorNota": -1,
             "menorNota": 99999,
             "quantidadeNotas": 0,
             "mediaTurma": 0,
             "totalNotas": 0}
    while r in 'Ssim':
        n = float(input('Qual foi a nota? '))
        r = str(input('Quer continuar? '))
        notas["quantidadeNotas"] += 1
        notas["totalNotas"] += n
        if n > notas["maiorNota"]:
            notas["maiorNota"] = n
        if n < notas["menorNota"]:
            notas["menorNota"] = n
    notas["mediaTurma"] = notas["totalNotas"] / notas["quantidadeNotas"]
    return notas


turma = tNotas()
print(f'Foram {turma["quantidadeNotas"]} alunos \n'
      f'A maior nota foi {turma["maiorNota"]}\n'
      f'A menor nota foi {turma["menorNota"]}\n'
      f'A media da turma foi {turma["mediaTurma"]}')
