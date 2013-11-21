def merge(input_array, beg, mid, end):
  """Merge procedure for merge sort algorithm"""
  listA = input_array[beg:mid+1]
  listB = input_array[mid+1:end+1]
  listC=[]
  while len(listA)>0 and len(listB)>0:
    if(listA[0]<listB[0]):
      listC.append(listA[0])
      listA.pop(0)
    else:
      listC.append(listB[0])
      listB.pop(0)
  listC+=listA
  listC+=listB
  input_array[beg:end+1]=listC
  pass

def msort(input_array, beg, end):
  """Main mergesort procedure"""
  # Boundary condition - subarray of size 1 is already sorted  
  if beg==end:
    return
  mid = int((beg+end)/2)
  msort(input_array, beg, mid)
  msort(input_array, mid+1, end)  
  merge(input_array, beg, mid, end)  # stub - merge the 2 halves together

def mergesort(input_array):
  """Wrapper for actual merge sort procedure"""
  array_length = len(input_array)
  msort(input_array, 0, array_length - 1)


number_of_input_values = int(raw_input())

current_input_position = 1
number_list=[]

for current_input_position in range(1, number_of_input_values+1):  
  current_input = int(raw_input())
  number_list.append(current_input)

mergesort(number_list)

for current_number in number_list:
  print current_number