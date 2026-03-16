#sorting and searching
#Apartments 

import sys

class Solution:
    def solve(self, n, m, k, applicants, apartments):
        result = 0

        # Write your logic here
        applicants.sort()
        apartments.sort()
        

        return result


def main():
    input = sys.stdin.readline
    
    n, m, k = map(int, input().split())
    applicants = list(map(int, input().split()))
    apartments = list(map(int, input().split()))
    
    sol = Solution()
    ans = sol.solve(n, m, k, applicants, apartments)
    
    print(ans)


if __name__ == "__main__":
    main()
