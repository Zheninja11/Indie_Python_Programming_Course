days = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve']
a = list(filter(lambda x: len(x) == 4 or x[0] == 'S', days))

print(*sorted(a), sep='\n')
