# https://leetcode.com/problems/campus-bikes-ii/
from scipy.optimize import linear_sum_assignment
import numpy as np

cost_mtx = [[999, 1000, 1001, 1002, 1003], [1000, 999, 1000, 1001, 1002], [1001, 1000, 999, 1000, 1001], [1002, 1001, 1000, 999, 1000], [1003, 1002, 1001, 1000, 999]]
cost_mtx = np.array(cost_mtx)
row_inds, col_inds = linear_sum_assignment(cost_mtx)

print(sum(cost_mtx[row_inds, col_inds]))
