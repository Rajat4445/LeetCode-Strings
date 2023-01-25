'''
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
'''
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        j = [j for j in jewels]    ## list(jewels) also works
        s = [s for s in stones]

        out = 0

        for i in j:
            out += s.count(i)

        return out
      
      
'''
You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.

 

Example 1:

Input: command = "G()(al)"
Output: "Goal"
Explanation: The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".
'''
o = ''

        for i in range(len(command)):                           ## Logic
            if command[i] == 'G':
                o += 'G'
            elif command[i] == '(' and command[i+1] == ')':
                o += 'o'
            elif command[i] == '(' and command[i+1] == 'a' and command[i+2] == 'l' and command[i+3] == ')':
                o += 'al'




