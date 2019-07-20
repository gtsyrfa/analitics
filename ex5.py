import pandas as pd
import os.path


def ex5(startfile: str,
        resultfile: str):

    if os.path.isfile(resultfile):
        print(f"Файл {resultfile} существует. Функция не будет выполнена!")
        return 0

    df = pd.read_excel(startfile, parse_dates=True)

    pvt = df.pivot_table(
        index=['date'],
        columns=['shop_id'],
        values=['turnover', 'pl_turnover']
    )

    # считаем разницу между планом и фактом
    pvt = (pvt['turnover'] - pvt['pl_turnover'])
    # заменяем всё, что больше/равно "0" на "+""
    pvt = pvt.mask(pvt >= 0, other="+")

    # записали в Excel
    writer = pd.ExcelWriter(resultfile, engine='xlsxwriter')
    pvt.to_excel(writer, startrow=0, header=True)
    writer.save()

if __name__ == "__main__":
    pass
    # ex5(r"files\analitics.xlsx", r"files\result5.xlsx")
