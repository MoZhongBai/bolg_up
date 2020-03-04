import linecache
import json
import random
def getline(the_file_path, line_number):
  if line_number < 1:
    return ''
  for cur_line_number, line in enumerate(open(the_file_path, 'rU')):
    if cur_line_number == line_number-1:
      return line
  return ''
# while True:
#     the_line = linecache.getline('user-agent.json',random.randint(1,1000))
#     print (json.loads(the_line))