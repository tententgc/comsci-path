def up_down(number: str):
  number_list = [int(i) for i in number]
  operations = ["<", ">"]
  for i in range(len(number_list)):
    if i + 1 >= len(number_list):
      break
    if eval(f"bool({number_list[i+1]} {operations[0]} {number_list[i]})"):
      return "False"
    operations = operations[::-1]
  return "True"
x = input()
print(up_down(x))