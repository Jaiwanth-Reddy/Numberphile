# Kaprekar

OEIS link for Four-digit numbers that do not resolve to 6174 https://oeis.org/A069746

OEIS link for Four-digit numbers that do not resolve to 495 https://oeis.org/A090429

First uploaded to github.com/scared-of-java which now is a shared account. Hence moved here.

Program to output steps taken to reach Kaprekar constant for each number, and other stats

The code loops through all 3 digit and 4 digit numbers, displaying steps taken to reach the constant, 6174 for 4 digit numbers, 495 for 3 digit numbers. 
If it does not follow the rule, that too is displayed.

The ouput.txt files have the ouput along with some stats at the end, which are -

The set of all exceptions.
Distribution of steps taken by the numbers.

# Summary of code output

Output_for_3_digit_nos.txt

The set of 60 Numbers Which Do Not Follow The Rule Are:

[100, 101, 110, 111, 112, 121, 122, 211, 212, 221, 222, 223, 232, 233, 322, 323, 332, 333, 334, 343, 344, 433, 434, 443, 444, 445, 454, 455, 544, 545, 554, 555, 556, 565, 566, 655, 656, 665, 666, 667, 676, 677, 766, 767, 776, 777, 778, 787, 788, 877, 878, 887, 888, 889, 898, 899, 988, 989, 998, 999]

Distribution of steps taken
{2: 138, 3: 131, 4: 246, 5: 198, 6: 126}

Output_for_4_digit_nos.txt

The set of 77 Numbers Which Do Not Follow The Rule Are:

[1000, 1011, 1101, 1110, 1111, 1112, 1121, 1211, 1222, 2111, 2122, 2212, 2221, 2222, 2223, 2232, 2322, 2333, 3222, 3233, 3323, 3332, 3333, 3334, 3343, 3433, 3444, 4333, 4344, 4434, 4443, 4444, 4445, 4454, 4544, 4555, 5444, 5455, 5545, 5554, 5555, 5556, 5565, 5655, 5666, 6555, 6566, 6656, 6665, 6666, 6667, 6676, 6766, 6777, 7666, 7677, 7767, 7776, 7777, 7778, 7787, 7877, 7888, 8777, 8788, 8878, 8887, 8888, 8889, 8898, 8988, 8999, 9888, 9899, 9989, 9998, 9999]

Distribution of steps taken
{2: 356, 3: 519, 4: 2124, 5: 1124, 6: 1311, 7: 1508, 8: 1980}
