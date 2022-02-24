a_input_str = 'a.txt'
a_output_str = 'A.txt'

b_input_str = 'b.txt'
B_output_str = 'B.txt'

c_input_str = 'c.txt'
C_output_str = 'C.txt'

d_input_str = 'd.txt'
D_output_str = 'D.txt'

e_input_str = 'e.txt'
E_output_str = 'E.txt'

# read from file
def text_to_list(tekst):
  podaci = []
  for red in tekst:
    podaci.append(red[:-1].split(" "))
  '''
  D, I, S, V, F = podaci[0][0], podaci[0][1], podaci[0][2], podaci[0][3], podaci[0][4]
  streets = podaci[1:int(S)+1]
  cars = podaci[int(S)+1:]
  return int(D), int(I), int(S), int(V), int(F), streets, cars
  '''
  return podaci

def read_from_file(file_name):
  with open(file_name, "r") as f:
    data = f.readlines()
  data = text_to_list(data)
  return data
#print(read_from_file(a_input_str)) 

# write to file
def write_to_file(file_name):
  with open(file_name, 'r') as original: data = original.read()
  with open(file_name, 'w') as modified: modified.write(str(9) + '\n' + data) 

# sorting function
#def score_reda(red):
#  skor = 0
#  for i in range(1, len(red)-1):
#    if red[i] in sastojci:
#      skor = skor + sastojci[red[i]][1]
#  return skor     
#podaci.sort(key=score_reda)