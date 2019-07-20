import pandas as pd
import os.path

# Задача довольно странная, с учётом того, что у меня есть первоначальный файл,
# откуда удобно вытащить информацию сразу в pivot table
# Поскольку выполняю задачу в выходные и не могу связаться, предполагаю,
# что у меня были два несведенных файла (задание то тестовое)
# Да и в принципе не совсем понятно, в каком виде должен получиться результат

def ex2(startfile: str,
        resultfile: str):

    if os.path.isfile(resultfile):
        print(f"Файл {resultfile} существует. Функция не будет выполнена!")
        return 0

    # вытащили результат первого задания
    df = pd.read_excel(startfile, parse_dates=True, index_col="date")

    # привели к результату первого задания таблицу с трафиком
    pvt = pd.read_excel(r"files\analitics.xlsx", parse_dates=True)
    pvt = pvt.pivot_table(
                          index=['date'],
                          columns=['shop_id'],
                          values='traffic')

    # сгруппировали по месяцу
    sample_df = df.resample('M').mean()
    sample_pvt = pvt.resample('M').mean()
    result_sample = sample_df.merge(sample_pvt, on='date',
                                    suffixes=("_tn", "_tr"))

    # записали в Excel
    writer = pd.ExcelWriter(resultfile, engine='xlsxwriter')
    result_sample.to_excel(writer, startrow=0, header=True)
    writer.save()

if __name__ == "__main__":
    pass
