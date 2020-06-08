# -*- coding: utf-8

"""
@File       :   MD_cal.py
@Author     :   Zitong Lu
@Contact    :   zitonglu1996@gmail.com
@License    :   MIT License
"""

import numpy as np
from scipy.spatial.distance import mahalanobis

def mahalanobis_distance(p, distr):

    # p: a point
    # distr : a distribution

    # covariance matrix
    cov = np.cov(distr, rowvar=False)

    # average of the points in distr
    avg_distri = np.average(distr, axis=0)

    dis = mahalanobis(p, avg_distri, cov)

    return dis