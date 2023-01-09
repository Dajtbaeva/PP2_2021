d = {
    ('Adil', 'Zhapar'): '20B8712398123',
    ('Asdfasdf', 'Vcxvb'): '19B8712398123',
    ('Gjosdufjlas', 'Zhapazxcvzxvr'): '20B8712398123',
    ('Ernat', 'Zhapar'): '18B8712398123',
}
res = sorted(d, key = lambda x : (x[1][:3], x[0][1]))