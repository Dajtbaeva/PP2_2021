import re
def checkleap(n):
    if (((n % 4 == 0) and (n % 100 != 0)) or (n % 400 == 0)):
        return False
    else: return True

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
         'August', 'September', 'October', 'November', 'December'] 

s = input()

if s[3:5] == '02':
    if s[0:2] == '29':
        if checkleap(int(s[6:])) == True:
            print('Year:', s[6:])
            print('Month: February', 'Day: 29', sep = '\n')
        else:
            print('-1')
    else:
        print('Year:', s[6:])
        print('Month: February')
        print('Day:', s[0:2])
elif s[3:5] == '01' or s[3:5] == '03' or s[3:5] == '05' or s[3:5] == '07' or s[3:5] == '08' or s[3:5] == '10' or s[3:5] == '12':
    pattern = r'(?P<day>0[1-9]|[1-2][0-9]|3[01])[:/;.](?P<month>0[1-9]|1[0-2])[:/;.](?P<year>19\d{2}|20[0-9]\d|2100)'
    if re.match(pattern, s):
        month = re.match(pattern, s).group("month")
        print('Year:', re.match(pattern, s).group("year"))
        print('Month:', months[int(month)])
        print('Day:', int(re.match(pattern, s).group("day")))
    else:
        print('-1')
else:
    pattern1 = r'(?P<day>0[1-9]|[1-2][0-9]|30)[:/;.](?P<month>0[1-9]|1[0-2])[:/;.](?P<year>19\d{2}|20[0-9]\d|2100)'
    if re.match(pattern1, s):
        month = re.match(pattern1, s).group("month")
        print('Year:', re.match(pattern1, s).group("year"))
        print('Month:', months[int(month)])
        print('Day:', int(re.match(pattern1, s).group("day")))
    else:
        print('-1')