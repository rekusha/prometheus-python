def bouquets(narcissus_price, tulip_price, rose_price, summ):
    counter = 0
    prices = sorted([narcissus_price, tulip_price, rose_price])
    maximum_quantity = int(round(summ / prices[0]))
    midlle_quantity = int(round(summ / prices[1]))
    minimum_quantity = int(round(summ / prices[2]))
    for i in range(maximum_quantity + 1):
        if i * prices[0] <= summ:
            ip = i * prices[0]
            for j in range(midlle_quantity + 1):
                if j * prices[1] + i * prices[0] <= summ:
                    jp = j * prices[1] + i * prices[0]
                    for k in range(minimum_quantity + 1):
                        if (jp + k * prices[2]) <= summ and (i + j + k) % 2 != 0:
                            counter += 1
    return counter