#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 14:59:38 2019

@author: blahoslav
"""
from six.moves import cPickle
import os
import six

if os.path.exists('/home/blahoslav/LM6D_refine_PoseCNN_val_ape_pose_iter4.pkl'):
        with open('/home/blahoslav/LM6D_refine_PoseCNN_val_ape_pose_iter4.pkl', "rb") as fid:
            if six.PY3:
                [all_rot_err, all_trans_err, all_poses_est, all_poses_gt] = cPickle.load(fid, encoding="latin1")
            else:
                [all_rot_err, all_trans_err, all_poses_est, all_poses_gt] = cPickle.load(fid)