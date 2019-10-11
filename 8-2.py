def find_fraction(summ):
    pivsumm = summ / 2
    if summ <= 2:
        return False
    if summ % 2 == 0:
        if pivsumm % 2 == 0:
            return (pivsumm - 1), (pivsumm + 1)
        else:
            return (pivsumm - 2), (pivsumm + 2)
    elif summ % 2 != 0:
        return (summ - 1) / 2, summ - (summ - 1) / 2