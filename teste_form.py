per = ['nome é:', 'a idade é:', 'sou téc de:']
res = [['josé', 'claudio', 'joão'],
       ['08', '19', '21'],
       ['ad', 'el', 'ed']]
gab = (3, 2, 2)
resp = list()
nota = int(0)

for r in range(len(per)):
    j = int(1)
    print(per[r])

    for i in range(len(res[r])):
        print(j, res[r][i])
        j += 1
    resp.insert(r, int(input('Escolha uma opção ')))
    if resp[r] == gab[r]:
        nota += 1

print(f'Sua nota foi {nota}')
