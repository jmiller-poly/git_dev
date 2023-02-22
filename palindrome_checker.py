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
    

def main()
