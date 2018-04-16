#!./ENV/bin python
# -*- coding: utf-8 -*-

'''
clean.py
- This script cleans the given .csv file.

Written by: Alex Wong
Date: Mar 26, 2018
'''

import collections
import regex


en_pattern = regex.compile(u'([a-zA-Z]+)', regex.UNICODE)
zh_pattern = regex.compile(u'([\p{IsHan}]+)', regex.UNICODE)
jp_pattern = regex.compile(u'([\p{IsHira}\p{IsKatakana}]+)', regex.UNICODE)
kr_pattern = regex.compile(u'([\p{IsHangul}]+)', regex.UNICODE)
num_pattern = regex.compile(u'([0-9]+)', regex.UNICODE)
bopo_pattern = regex.compile(u'[\p{IsBopo}]', regex.UNICODE)
patterns = [en_pattern, zh_pattern, jp_pattern, kr_pattern, num_pattern, bopo_pattern]

dic = collections.defaultdict(list)
dic['zh'] = [False, True, False, False, False, False]  # zh
dic['zh_num'] = [False, True, False, False, True, False]  # zh, nums
dic['en'] = [True, False, False, False, None, False]  # en, {nums}
dic['jp'] = [False, False, True, False, None, False]  # jp, {nums}
dic['kr'] = [False, False, False, True, None, False]  # kr, {nums}
dic['zh_any'] = [None, True, None, None, None, None]

def match_pattern(data, founds):
    """
    Check data to match all the patterns.
    :param data: string
    :param patterns: list of regex.compile patterns
    :param founds: list of booleans/None. True: exist, False: not exist, None: optional
    :return: boolean
    """
    for i in range(len(patterns)):
        if founds[i] is None:
            continue
        elif founds[i] != (patterns[i].search(data) is not None):
            return False
    return True

def pattern_worker(data_inputs, codes):
    """
    Check data to match all the patterns.
    :param data_inputs: string array
    :param codes: list of {'zh' | 'zh_num' | 'en' | 'jp' | 'kr'}
    :return: void
    """
    for code in codes:
        for data_input in data_inputs:
            if match_pattern(data_input, dic[code]):
                print(data_input)