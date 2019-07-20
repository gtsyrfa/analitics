import pandas as pd
import os.path

# "А Слава КСПП вообще не человек"
# (Из старого анекдота про чукчу, к рэперу отношения не имеет)
# На самом деле, есть некоторая неоднозначность в заданях,
# и прошлые задачи я делал,
# предполагая более сложный сценарий.
# Тут уж я не представляю, как из, так сказать,
# "сжатия с потерей" восстановить утерянные значения
# (не делить же на 4, чтобы получить из месяца неделю)
# поэтому пойду по "реализуемому" сценарию


def ex3(startfile: str,
        resultfile: str):
    # вытащили результат первого задания
    df = pd.read_excel(startfile, parse_dates=True, index_col="date")

    if os.path.isfile(resultfile):
        print(f"Файл {resultfile} существует. Функция не будет выполнена!")
        return 0

    # привели к результату задания таблицу с трафиком
    pvt = pd.read_excel(r"files\analitics.xlsx", parse_dates=True)
    pvt = pvt.pivot_table(
                          index=['date'],
                          columns=['shop_id'],
                          values='traffic')

    # сгруппировали по неделе
    sample_df = df.resample('W').mean()
    sample_pvt = pvt.resample('W').mean()
    result_sample = sample_df.merge(sample_pvt, on='date',
                                    suffixes=("_tn", "_tr"))

    # записали в Excel
    writer = pd.ExcelWriter(resultfile, engine='xlsxwriter')
    result_sample.to_excel(writer, startrow=0, header=True)
    writer.save()

if __name__ == "__main__":
    pass
