import sys

def solve():
\
    for line in sys.stdin:
        s = line.strip()
        if not s:
            continue
            
        target = "hackerrank"
        target_len = len(target)
        target_ptr = 0
        
   
        for char in s:
            if char == target[target_ptr]:
                target_ptr += 1
                if target_ptr == target_len:
                    break
        
        if target_ptr == target_len:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()
