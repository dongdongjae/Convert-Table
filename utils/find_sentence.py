import pandas as pd

file_kb_test_path = './kb_v2.0.0_test.xlsx'

tb_sent = pd.read_excel(file_kb_test_path, 'sent')
tb_sent.set_index('sentence_id', inplace=True)

def find_sentence(sentence_id):
    return [sentence_id, tb_sent.loc[sentence_id, 'sentence_kor']]