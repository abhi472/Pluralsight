scientist = ['mariecurie', 'pierrecurie', 'issacasimov', 'nikoltesla', 'johnnash']



print(sorted(scientist, key=lambda name: name.split()[-1]))
