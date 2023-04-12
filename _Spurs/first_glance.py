#!/usr/bin/python3

def show_empty_spaces(df_: object) -> object:
    ''' Показывает пустые ячейки в таблице по признакам
    Arguments:
        df_ [DataFrame] -- Анализируемый датасет
    Returns:
        [Series] -- Количество пустых значений по признакам
    '''
    # REQUIRES:
    # import pandas
    return df_.isna().sum(axis='index')

if __name__ == '__main__':
    # import pandas as pd
    # DF = pd.DataFrame(data={'foo': [1], 'bar': [0]})
    # print(show_empty_spaces(DF))
    print('Import this module rather than run it!')

#####=====----- THE END -----=====#####