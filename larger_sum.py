def larger_sum(lst1, lst2):
  num = 0
  var = 0
  while num < len(lst1):
    var = lst1[num] + var
    num = num + 1
  nums = 0 
  var_2 = 0
  while nums < len(lst2):
    var_2 = lst2[nums] + var_2
    nums = nums + 1 
  if var >= var_2:
    return lst1
  if var_2 > var:
    return lst2

print(larger_sum([1, 9, 5, 3, 7, 1 ,5, 8], [2, 3, 7, 13, 5, 8, 6, 14]))