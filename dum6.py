class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, index, val):
        while index <= self.n:
            self.bit[index] += val
            index += index & -index

    def get_sum(self, index):
        total = 0
        while index > 0:
            total += self.bit[index]
            index -= index & -index
        return total

def assign_hotels(n, m, hotels, groups):
    # Initialize the Fenwick Tree
    bitree = FenwickTree(n)

    # Initialize the assigned hotel array
    assigned_hotel = [0] * m

    # Create a list of tuples (hotel index, free rooms) and sort by free rooms
    sorted_hotels = sorted(enumerate(hotels), key=lambda x: x[1])

    # Assign groups to hotels
    for group_idx, rooms_required in enumerate(groups):
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if sorted_hotels[mid][1] >= rooms_required:
                assigned_hotel[group_idx] = sorted_hotels[mid][0] + 1
                bitree.update(sorted_hotels[mid][0] + 1, -1)  # Decrease free rooms
                right = mid - 1
            else:
                left = mid + 1

    return assigned_hotel

# Input
n, m = map(int, input().split())
hotels = list(map(int, input().split()))
groups = list(map(int, input().split()))

# Get the assigned hotel for each group
result = assign_hotels(n, m, hotels, groups)

# Print the result
print(*result)
