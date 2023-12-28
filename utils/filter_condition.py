def filter_condition(arr):
    result_arr = []
    
    for i_idx, i in enumerate(arr[0]):
        if i == 0:
            continue
        for j_idx, j in enumerate(arr[1]):
            if j == 0:
                continue
            for k_idx, k in enumerate(arr[2]):
                if k == 0:
                    continue
                
                C_01 = 1 if i_idx == 0 else 2
                C_02 = 1 if j_idx == 0 else 2
                C_03 = 1 if k_idx == 0 else 2
                result_arr.append([C_01, C_02, C_03])
    
    return result_arr