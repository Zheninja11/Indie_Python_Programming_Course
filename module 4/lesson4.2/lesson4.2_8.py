boys_count = int(input())
boys_list = list(map(int, input().split()))
boys_list.sort()
girls_count = int(input())
girls_list = list(map(int, input().split()))
girls_list.sort()
boys = 0
girls = 0
count = 0
while boys_list != [] and girls_list != []:
    if abs(boys_list[boys] - girls_list[girls]) <= 1:
        count += 1
        boys_list.pop(boys_list.index(boys_list[boys]))
        girls_list.pop(girls_list.index(girls_list[girls]))
    else:  # Иначе
        if boys_list[boys] > girls_list[
            girls]: 
            girls_list.pop(girls_list.index(girls_list[girls]))
        else:
            boys_list.pop(boys_list.index(boys_list[boys]))  
print(count)
