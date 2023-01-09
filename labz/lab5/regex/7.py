import re
print(''.join(x.capitalize() or '_' for x in input().split('_')))
# i_learn_python -> ILearnPython