def avg(x,*more):
    return (x + sum(more)) / (1 + len(more))
print(avg(10,11,12))  # 11.0
print(avg(10,11,12,13,14))  # 12.0