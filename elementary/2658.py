map_list = [input().strip() for _ in range(10)]

def find_rectangle() :
  min_x, min_y = 10, 10
  max_x, max_y = -1, -1

  for i in range(10) :
    for j in range(10) :
      if map_list[i][j] == '1' :
        min_x = min(min_x, j)
        max_x = max(max_x, j)
        min_y = min(min_y, i)
        max_y = max(max_y, i)

  return (min_x, max_x), (min_y, max_y)

def find_all_vertexs(x_tuple, y_tuple) :
  result = set()
  
  for j in x_tuple :
    tmp = list()
    for i in range(10) :
      if map_list[i][j] == '1' :
        tmp.append((i+1, j+1))
    if tmp :
      result.add(tmp[0])
      result.add(tmp[-1])

  for i in y_tuple :
    tmp = list()
    for j in range(10) :
      if map_list[i][j] == '1' :
        tmp.append((i+1, j+1))
    if tmp :
      result.add(tmp[0])
      result.add(tmp[-1])

  result = list(result)
  result.sort()
  
  return result

def square_length(a, b) :
  return (a[0] - b[0])**2 + (a[1] - b[1])**2

def is_correct(x_tuple, y_tuple) :
  min_x, max_x = x_tuple
  min_y, max_y = y_tuple

  len_list = list()
  for i in range(min_y, max_y+1) :
    tmp = list()
    for j in range(min_x, max_x+1) :
      if map_list[i][j] == '1' :
        tmp.append(j)
    if tmp :     
      if len(tmp) != tmp[-1] - tmp[0] + 1 :
        return False
      len_list.append(len(tmp))

  if not len_list :
    return False
    
  max_idx = len_list.index(max(len_list))
  if max_idx > 0 :
    upper_diff = len_list[max_idx] - len_list[max_idx-1]
    for i in range(max_idx) :
      if len_list[i+1] - len_list[i] != upper_diff :
        return False

  if max_idx < len(len_list) - 1 :
    lower_diff = len_list[max_idx] - len_list[max_idx+1]
    for i in range(max_idx, len(len_list)-1) :
      if len_list[i] - len_list[i+1] != lower_diff :
        return False

  return True

def is_irt(vertex_list) :
  if len(vertex_list) != 3 :
    return False
    
  a, b, c = vertex_list
  line_list = [ square_length(a, b), square_length(b, c), square_length(c, a) ]
  line_list.sort()
  
  return line_list[0] == line_list[1] and line_list[0] + line_list[1] == line_list[2]


def solve() :
  x_tuple, y_tuple = find_rectangle()
  if x_tuple == (10, -1) :
    print(0)
    return
  
  vertex_list = find_all_vertexs(x_tuple, y_tuple)

  if is_irt(vertex_list) and is_correct(x_tuple, y_tuple) :
    for vertex in vertex_list: print(*vertex)
  else: print(0)

solve()