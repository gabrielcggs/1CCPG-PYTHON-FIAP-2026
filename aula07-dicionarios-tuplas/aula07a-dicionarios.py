eng2sp = dict()
print(eng2sp)

eng2sp['one'] = 'uno'
print(eng2sp)

eng2sp = {
    'one': 'uno',
    'two': 'dos',
    'three': 'tres'
}
print(eng2sp)
print(eng2sp['one'])
print(eng2sp['two'])
print(eng2sp['three'])

print('dos' in eng2sp)

valores = eng2sp.values()
print('uno' in valores)

print("==============")

def count_letters(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

dict_contagem = count_letters("ovo")
print(dict_contagem)