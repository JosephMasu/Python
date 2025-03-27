import time

def net_price(list_price, discount, tax):
    return list_price * (1 - discount) * (1 + tax)
print(f"{net_price(500,0.0001, 0.015):.2f}")

def count(end, start= 0):
    for i in range(start, end):
        print(i)
        time.sleep(1)
    print("DONE!")

count(30, 15)
