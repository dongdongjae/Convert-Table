import pandas as pd
import numpy as np
from utils.filter_condition import filter_condition
from utils.find_sentence import find_sentence


file_kb_test_path = './kb_v2.0.0_test.xlsx'

# tb_cond = pd.read_excel(file_kb_test_path, 'cond')
# tb_sent = pd.read_excel(file_kb_test_path, 'sent')
tb_map = pd.read_excel(file_kb_test_path, 'map')
# tb_list = pd.read_excel(file_kb_test_path, 'list')

result_data = {'idx': [], 'C01': [], 'C02': [], 'C03': [],
               'sentence_id': [], 'sentence_kor': []}


def main():
    map_row_head = tb_map.iloc[:, 0]
    map_row_tail = tb_map.iloc[:, 1:]

    map_row_tail = map_row_tail.applymap(lambda x: 1 if x == "Y" else 0).values

    

    map_row_paired_list = np.stack(
        (map_row_tail[:, ::2], map_row_tail[:, 1::2]), axis=-1)

    conditions_data_list = [filter_condition(
        ex_arr) for ex_arr in map_row_paired_list]

    sentence_data_list = [find_sentence(id) for id in map_row_head]

    for i_idx, i in (enumerate(sentence_data_list)):
        for j in (conditions_data_list[i_idx]):
            result_data['sentence_id'].append(i[0])
            result_data['sentence_kor'].append(i[1])
            result_data['C01'].append(j[0])
            result_data['C02'].append(j[1])
            result_data['C03'].append(j[2])

    for idx in range(len(result_data['C01'])):
        result_data['idx'].append(idx+1)
        
    result_df = pd.DataFrame(result_data)


    with pd.ExcelWriter(file_kb_test_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        result_df.to_excel(
            writer, sheet_name='list', index=False)

if __name__ == "__main__":
    main()
