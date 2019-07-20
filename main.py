from ex1 import ex1
from ex2 import ex2
from ex3 import ex3
from ex4 import ex4
from ex5 import ex5
import time

def main():
    ex1(r"files\analitics.xlsx", r"files\result1.xlsx")
    ex2(r"files\result1.xlsx", r"files\result2.xlsx")
    ex3(r"files\result1.xlsx", r"files\result3.xlsx")
    ex4(r"files\analitics.xlsx", r"files\result4.xlsx")
    ex5(r"files\analitics.xlsx", r"files\result5.xlsx")

if __name__ == "__main__":
    start_time = time.time()
    main()
    print(time.time() - start_time)