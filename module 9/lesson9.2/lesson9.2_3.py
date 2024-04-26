def find_lines_len_more_6(file_name:str) -> int:
    
    with open(file_name, 'r') as f:
        cnt = 0
        f = f.readlines()
        for i in f:
            if len(x:=i.replace('\n','')) > 6:
                cnt += 1
        return cnt
