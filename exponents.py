# This program takes in a list of bases and powers, and raises each base to each power, creating a list of every possible combination
def exponents(bases, powers):
  bases_raised = []
  i = 0
  for num in bases:
    var = bases[i]
    nums = 0
    while nums < len(powers):
      var_2 = powers[nums]
      base_x_power = var ** var_2
      bases_raised.append(base_x_power)
      nums = nums + 1
    i = i + 1
  return bases_raised

print(exponents([2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
