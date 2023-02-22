#!/usr/bin/env python3
"""
palindrome_checker.py
A class for checking if something is a palindrome
"""

from atds import Dequeue as DEQ

class PalindromeChecker:
    def __init__(self):
        self.strict_mode = False

    def set_strict_mode(self, setting):
        self.strict_mode = setting

    def is_palindrome(self, phrase):
        q = DEQ()
        if self.strict_mode:
            for chr in phrase:
                q.add_front(chr)
        else:
            for chr in phrase.lower():
                if chr in "abcdefghijklmnopqrstuvwxyz":
                    q.add_front(chr)
        
        while q.size() > 1:
            if q.remove_front() != q.remove_rear():
                return False

        return True
    

def main():
    checker = PalindromeChecker
    
    for_checking = ["aba", "abba", "a_ bb +a", "bba"]

    for fc in for_checking:
        print("Palindrome checker!")
        print("Strict mode is: " + checker.strict_mode)
        print("phrase: " + fc)
        if checker.is_palindrome(fc):
            print("It is a palindrome!")
        else:
            print("Not a palindrome.")
    checker.set_strict_mode(True)
    for fc in for_checking:
        print("Palindrome checker!")
        print("Strict mode is: " + checker.strict_mode)
        print("phrase: " + fc)
        if checker.is_palindrome(fc):
            print("It is a palindrome!")
        else:
            print("Not a palindrome.")
    
if __name__ == "__main__":
    main()