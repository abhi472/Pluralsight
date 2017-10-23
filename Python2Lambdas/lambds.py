scientist = ['mariecurie', 'pierrecurie', 'issacasimov', 'nikoltesla', 'johnnash']



print(sorted(scientist, key=lambda name: name.split()[-1]))

key = lambda name : name.split()[-1]
print(key("nikola tesla"))