import re 
s = input()
pattern = r'\W*\d*(?P<nuzhno>[a-z]+_[a-z]+).*' 
 
if re.search(pattern, s) != None:
    print(re.search(pattern, s).group('nuzhno'))
else:
    print('Ne naideno')
# abc_defg -> abc_defg 
# Pavlodar_taraZ -> avlodar_tara 
# 12ILo_vePy9thon -> o_ve 