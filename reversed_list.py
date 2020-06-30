# This program takes in 2 lists and compares them to see if the other list is equal to the first list reveresed
def reversed_list(lst1, lst2):
  i = 0
  t_o_f = True
  for value in range(len(lst1)):
    if t_o_f == False:
      break
    var = lst1[i]
    var2 = lst2[-i -1]
    if var != var2:
      t_o_f = False
    i = i + 1
  return t_o_f

print(reversed_list([1, 2, 3, 5, 6, 2, 4,], [4, 2, 6, 5, 3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))
