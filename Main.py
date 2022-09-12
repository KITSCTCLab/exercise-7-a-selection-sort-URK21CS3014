from typing import List

def selectionSort(array, size) -> List[int]:
  for i in range[size-2]:
    min=i
    for j in range[size-1]:
      if array[min]>array[j]:
        min=j
    temp=array[i]
    array[i]=array[min]
    array[min]=temp

# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
