# User function Template for python3

class Solution:
    def removeStudents(self, H, N):
        cnt = 0
        i = 0
        while i < N - 1:
            if H[i] >= H[i + 1]:
                cnt += 1
            i += 1
        return cnt


# code here


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        H = list(map(int, input().split()))

        ob = Solution()
        print(ob.removeStudents(H, N))
# } Driver Code Ends
