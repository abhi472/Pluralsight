from pprint import pprint  as pp

store = []
def local_fuction_sorting(strings):
    def srting(s):
        return s[-1]
    store.append(srting)
    return sorted(strings, key=srting)

print(local_fuction_sorting(['hello', 'from', 'the', 'other', 'side']))
print(local_fuction_sorting(['load', 'up', 'on', 'guns', 'bring','your', 'friends', 'it\'s', 'fun', 'to','lose', 'and', 'to','pretend']))

pp(store)   # this shows that each call to local_function_sorting creates new instance of srting