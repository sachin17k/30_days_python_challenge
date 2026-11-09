siblings = ()
brothers = ('alan','AURA')
sisters = ('anusha',)
siblings = brothers + sisters
print(siblings)
print(f"i have {len(siblings)} number of siblings")
siblings_list = list(siblings)
siblings_list.append('kumar')
siblings_list.append('suganthi')
siblings = tuple(siblings_list)
family = siblings
print(f"My family {family}")

#exersise two:

siblings = family[:3]
parents = family[-2:]
print(f"siblings:{siblings}\n parents:{parents}")
del parents


nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print(f"estonia in nordic countries:{'estonia' in nordic_countries}")
print(f"estonia in nordic countries:{'Norway' in nordic_countries}")
