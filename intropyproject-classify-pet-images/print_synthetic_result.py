#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# print_synthetic_results.py

def print_synthetic_result(results_stats_dic, model):
    len_coln1 = len("# Not-a-Dog Images") + 2
    len_coln2 = 4
    len_total = len_coln1 + len_coln2 + 7
    print("-" * (len_total))
    print("| {0:>{2}} | {1:^{3}} |".format("# Total Images", results_stats_dic['n_images'], len_coln1, len_coln2))
    print("| {0:>{2}} | {1:^{3}} |".format("# Dog Images" ,results_stats_dic['n_dogs_img'], len_coln1, len_coln2))
    print("| {0:>{2}} | {1:^{3}} |".format("# Not-a-Dog Images", results_stats_dic['n_notdogs_img'], len_coln1, len_coln2))
    print("-" * len_total)

    len_stats_len = len("CNN Model Architecture:") + len("% Not-a-Dog Correct") + len("% Dogs Correct") + len("% Breeds Correct") + len("% Match Labels") + 5 * 2 + 6
    len_stats_coln1 = len("CNN Model Architecture:")
    len_stats_coln2 = len("% Not-a-Dog Correct")
    len_stats_coln3 = len("% Dogs Correct")
    len_stats_coln4 = len("% Breeds Correct")
    len_stats_coln5 = len("% Match Labels")

    print("-" * len_stats_len)
    print("| {} | {} | {} | {} | {} |".format("CNN Model Architecture:", "% Not-a-Dog Correct", "% Dogs Correct", "% Breeds Correct", "% Match Labels"))
    print("-" * len_stats_len)
    print("| {0:>{1}} | {2:>{3}} | {4:>{5}} | {6:>{7}} | {8:>{9}} |".format(model, len_stats_coln1, round(results_stats_dic['pct_correct_notdogs'], 1), len_stats_coln2, round(results_stats_dic['pct_correct_dogs'], 1), len_stats_coln3, round(results_stats_dic['pct_correct_breed'], 1), len_stats_coln4, round(results_stats_dic['pct_match'], 1), len_stats_coln5))
    print("-" * len_stats_len)
