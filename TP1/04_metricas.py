###
def r_precision(g, r):
    return len(set(pl_eval).intersection(r)) / len(pl_eval)


pl_train = [1,2,3]
pl_eval = [4, 5]
r = [4, 8, 12, 40, 100, 102]

r_precision(pl_eval, r)
    

