# -*- coding: utf-8 -*-

from scraping import SubtoCSV
from subComparer import SubCompare


#print("Enter two subs to compare")
#thisSub = input()
sub1 = "Music"
sub2 = "industrialmusic"
#SubtoCSV(sub1)
SubtoCSV(sub2)
SubCompare(sub1, sub2)