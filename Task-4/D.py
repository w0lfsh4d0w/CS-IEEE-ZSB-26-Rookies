import math

def solve():
    s1 = input()
    s2 = input()
    
    target = s1.count('+') - s1.count('-')
    current = s2.count('+') - s2.count('-')
    k = s2.count('?')

    def count_ways(remaining_k, current_pos):
        if remaining_k == 0:
            return 1 if current_pos == target else 0
        
        return count_ways(remaining_k - 1, current_pos + 1) + \
               count_ways(remaining_k - 1, current_pos - 1)

    successful_ways = count_ways(k, current)
    total_possibilities = 2 ** k
    
    probability = successful_ways / total_possibilities
    print(f"{probability:.12f}")

solve()
    
    