import re
print(re.sub(r'(\w)([A-Z])', r'\1 \2', input())) 
# ILovePython -> I Love Python
