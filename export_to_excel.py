import pandas as pd
import xlsxwriter
import os.path


def export_to_excel(var_data: pd.DataFrame,
                    var_mask: pd.DataFrame,
                    var_outfile: str,
                    var_compare):

    if os.path.isfile(var_outfile):
        print(f"Файл {var_outfile} существует. Функция не будет выполнена!")
        return 0

    if not len(var_data.index) == len(var_mask.index):
        print("Количество строк у var_data и var_mask различная. ",
              "Функция не будет выполнена!")
        return 0

    if not len(var_data.columns) == len(var_mask.columns):
        print("Количество столбцов у var_data и var_mask различается. ",
              "Функция не будет выполнена!")
        return 0

    # Переменные, необходимые для работы экселя.
    writer = pd.ExcelWriter(var_outfile, engine='xlsxwriter')
    var_data.to_excel(writer, startrow=0, header=True, sheet_name='Sheet1')
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']

    for cur_string in range(len(var_data.index)):

        tmp_series_value = var_data.iloc[cur_string]
        tmp_series_mask = var_mask.iloc[cur_string]

        # После первого "for" сохраняем строки.
        # Второй "for" нужен, чтобы вытаскивать значения из столбцов
        for cur_row in range(len(tmp_series_value.index)):

            value = tmp_series_value.iloc[cur_row]
            mask = tmp_series_mask.iloc[cur_row]

            if mask < var_compare:
                ft = workbook.add_format({'bg_color': 'red'})

            else:
                ft = workbook.add_format({'bg_color': 'green'})

            # Прибавляем по еднице потому что в экселе нумерация не с "0"
            # начинается, а с "1"
            worksheet.write(cur_string+1, cur_row+1,  value, ft)
    writer.save()

if __name__ == "__main__":
    pass
