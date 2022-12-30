prato = ('pizza','hamburguer','pastel')
price = (30,8,5)

print('{:#^30}'.format(' MENU '))
for c in range(0,3):
    print('{:.<20}R$ {}'.format(prato[c],price[c]))
print('{:#^30}'.format(' MENU '))
