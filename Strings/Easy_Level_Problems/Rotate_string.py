# Problem : Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

def Rotation(s, goal):
    if len(s) != len(goal):
        return False
    double_s = s+s
    if goal in double_s:
        return True
    return False

#Example Usage
if __name__ == "__main__":
    s = "abcde"
    goal = "cdeab"
    print(Rotation(s, goal))
    s = "abcde"
    goal = "abced"
    print(Rotation(s, goal))