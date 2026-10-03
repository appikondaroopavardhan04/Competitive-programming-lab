import sys

def solve():
    # Read all tokens from standard input efficiently
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    
    try:
        # The very first integer is the total number of test cases (T)
        T = int(next(iterator))
    except StopIteration:
        return
        
    for _ in range(T):
        try:
            # Each test case begins with its grid size N
            N = int(next(iterator))
        except StopIteration:
            break
        
        # Build the N x N grid
        grid = []
        for _ in range(N):
            row = [int(next(iterator)) for _ in range(N)]
            grid.append(row)
            
        # Initialize DP table with infinity
        dp = [[float('inf')] * N for _ in range(N)]
        
        # Base case
        dp[0][0] = grid[0][0]
        
        # Fill the DP table
        for i in range(N):
            for j in range(N):
                if i == 0 and j == 0:
                    continue
                
                min_prev = float('inf')
                
                # Check Up neighbor (Down move)
                if i > 0:
                    min_prev = min(min_prev, dp[i-1][j])
                # Check Left neighbor (Right move)
                if j > 0:
                    min_prev = min(min_prev, dp[i][j-1])
                # Check Diagonal neighbor (Diagonal move)
                if i > 0 and j > 0:
                    min_prev = min(min_prev, dp[i-1][j-1])
                    
                dp[i][j] = grid[i][j] + min_prev
        
        # Print the minimum path cost to match the sample outputs
        print(dp[N-1][N-1])

if __name__ == '__main__':
    solve()
