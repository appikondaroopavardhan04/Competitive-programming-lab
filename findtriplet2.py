import sys

def find_triplets_naive():
    
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    
    N = int(input_data[0])
    arr = [int(x) for x in input_data[1:N+1]]
    X = int(input_data[N+1])

    unique_triplets = set()

    
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                if arr[i] + arr[j] + arr[k] == X:
                    
                    triplet = tuple(sorted([arr[i], arr[j], arr[k]]))
                    unique_triplets.add(triplet)

    
    if not unique_triplets:
        print("No Triplet Found")
    else:
        
        for triplet in sorted(unique_triplets):
            print(f"{triplet[0]} {triplet[1]} {triplet[2]}")

if __name__ == '__main__':
    find_triplets_naive()
