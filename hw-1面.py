# 合并区间
def merge(intervals):
    intervals.sort(key = lambda x:x[0])

    res = []
    for inte in intervals:
        if not res or res[-1][1] < inte[0]:
            res.append(inte)
        else:
            res[-1][1] = inte[1]

    return res

intervals = [[1,3],[2,6],[8,10],[15,18]] #[[1, 4], [4, 5]]

print(merge(intervals))