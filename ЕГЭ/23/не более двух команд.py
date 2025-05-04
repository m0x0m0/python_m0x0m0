def fn(a, b, mult): #mult - число команд умножения
  if a == b and mult <= 2:
      return 1
  if a > b:
      return 0
  if mult == 2:
      return fn(a + 1, b, mult) + fn(a + 2, b, mult) #если 2 команды умножения, то выполнять только сложение
  return fn(a + 1, b, mult) + fn(a + 2, b, mult) + fn(a * 2, b, mult + 1)+ fn(a * 4, b, mult + 1) # осн. команды
print(fn(1, 13, 0))