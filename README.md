# CENG111-THE3-Tester
Tester for the CENG111 Take Home Exam 3 in 2020-21 Fall Semester.


To use this tester:

    Put the3.py and these files in the same directory.
    And run tester.py!
    

In case of errors similar to "ModuleNotFoundError: No module named 'the3'", modify the second line of tester.py, which imports your the3.py
    
     for e.g:  If your the3.py is in a folder named CENG_111_THE3, 
               modify the line respect to it's path 
               from CENG_111_THE3.the3 import *
     If you are using VSCode, you may need to write file's path completely


Tester prints all of the cases (True or False) on results.txt. Terminal just shows your score.

You can use tester_short.txt for easier analyzing the cases.
To do that, just change the file name at the sixth line.
You can also check out our other cases with different lengths.
(Beware the file tester_unnecessary_long.txt, it contains 12 MBs of data, which takes a minute or two to process depending on your code and computer.)

If you wonder how we generated our cases, you can check out case_generator.py.
case_generator.py overwrites our cases, in that case you can just download our tester.txt file again.

Expected results are calculated with respect to our outputs. If you think they are incorrect, please contact us and share your output.

Coded by:
# Baran Yancı
# Taner Sarp Tonay


