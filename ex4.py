import pandas as pd
import os.path

# По заданию надо посчитать значение среднего чека.
# Оно уже есть в первоначальном файле.
# Поэтому использую существующее значение. После выполнения первого задания,
# такой расчёт мне не кажется сложным.

def ex4(startfile: str,
        resultfile: str):

    if os.path.isfile(resultfile):
        print(f"Файл {resultfile} существует. Функция не будет выполнена!")
        return 0

    df = pd.read_excel(startfile, parse_dates=True)

    # Составили сводную таблицу
    pvt = df.pivot_table(
        index=['date'],
        columns=['shop_id'],
        values='av_check'
    )

    # Добавили значение суммы за день
    pvt['avg'] = pvt.mean(axis=1)

    # записали в Excel
    writer = pd.ExcelWriter(resultfile, engine='xlsxwriter')
    pvt.to_excel(writer, startrow=0, header=True)
    writer.save()

if __name__ == "__main__":
    pass
