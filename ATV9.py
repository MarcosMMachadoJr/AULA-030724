codigo, quantidade = input().split()
codigo = int(codigo)
quantidade = int(quantidade)
if codigo == 1:
  print('Total: R$ {:.2f}'.format(8.00 * quantidade))
elif codigo == 2:
  print('Total: R$ {:.2f}'.format(12.00 * quantidade))
elif codigo == 3:
  print('Total: R$ {:.2f}'.format(16.00 * quantidade))
