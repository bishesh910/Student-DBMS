import unittest
import hi
from tkinter import *
rootval= Tk()
a=hi.SMS(rootval)
class Test_hi(unittest.TestCase):
    def test_search(self):
        array_test = [('1', 'Bishesh', 'Shrestha', '19', 'Chabahil', 'Ethical hacking and cybersecurity'),
                      ('2', 'Riya', 'Shrestha', '19', 'Immadol', 'Ethical hacking and cybersecurity'),
                      ('3', 'sayhan', 'Shrestha', '19', 'nakhu', 'Ethical hacking and cybersecurity')]
        ex_result = [('2', 'Riya', 'Shrestha', '19', 'Immadol', 'Ethical hacking and cybersecurity')]
        a.entrysearch.delete(0, 'end')
        a.searchbyCB.set('FirstName')
        a.entrysearch.insert(0, 'Riya')
        ac_result = a.search_item(array_test)
        print("search test")
        print(ac_result)
        self.assertEqual(ex_result, ac_result)

    def test_bubble_sort(self):
        array_test=[('2','Riya','Shrestha','19','Immadol','Ethical hacking and cybersecurity'),('1','Bishesh','Shrestha','19','Chabahil','Ethical hacking and cybersecurity')]
        ex_result=[('1','Bishesh','Shrestha','19','Chabahil','Ethical hacking and cybersecurity'),('2','Riya','Shrestha','19','Immadol','Ethical hacking and cybersecurity')]
        a.sortord.set("ASC")
        a.searchbyCB.set("ID")

        ac_result=a.bubble_sort(array_test)
        print('Sort test')
        print(ac_result)
        self.assertEqual(ex_result,ac_result)




if __name__=='__main__':
    unittest.main()