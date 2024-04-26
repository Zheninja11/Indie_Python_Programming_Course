assert 200 > 100 # ok                            
assert [100] * 4 < [100, 100, 100, 10000]  # ok
assert sum([3, 2]) != sum([6, 3]) # ok            
assert max(3, -1, 9) == 9   #                 
print('Проверки пройдены')
