def saddle_point(matrix):

    count, last = 0, 0;
    for i in matrix:
        if i.count(min(i)) == 1:
            m = i.index(min(i));
            col = [];
            for j in matrix:
                col.append(j[m]);
            if col.count(max(col)) == 1 and min(i) == max(col):
                result = (int(m), int(col.index(max(col))));
                count += 1;
        if count > last:
            last = count;
            return result;
    if count == 0:
        return False;