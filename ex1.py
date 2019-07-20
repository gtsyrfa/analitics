import pandas as pd
from export_to_excel import export_to_excel
import os.path

def ex1(startfile: str,
        resultfile: str):
    
    if os.path.isfile(resultfile):
        print(f"Файл {resultfile} существует. Функция не будет выполнена!")
        return 0
    # При импорте файла решил оставить "несоответствие" количества знаков
    # после запятой у среднего чека. Так точнее выйдет.
    df = pd.read_excel(startfile, parse_dates=True)

    # считаем процент соблюдения плана
    df['turnover_percent'] = df['turnover']/df['pl_turnover']*100

    pvt = df.pivot_table(
        index=['date'],
        columns=['shop_id'],
        values='turnover'
    )

    pvt_percent = df.pivot_table(
        index=['date'],
        columns=['shop_id'],
        values='turnover_percent'
    )
    export_to_excel(pvt, pvt_percent, resultfile, 97.0)

if __name__ == "__main__":
    pass
