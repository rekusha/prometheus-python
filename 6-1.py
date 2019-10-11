def count_holes(n):

    if type(n) != int and type(n) != str and type(n) != long:
        return 'ERROR'
    else:
        try:
            num_dictitionary = {'0' : 1, '4' : 1, '6' : 1, '8' : 2, '9' : 1};
            counter = 0;
            n = int(n);
            n = str(n);
            for i in n:
                if i in num_dictitionary:
                    counter = counter + num_dictitionary.get(i);
            return counter;
        except ValueError:
            return 'ERROR'
        except TypeError:
            return 'ERROR'