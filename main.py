import itertools


def all_permutations(lst):
    # Generate all permutations
    all_permutations = set(itertools.permutations(lst))
    return all_permutations


def expand_siteswap(original_list, max_value, target_sum):
    n = len(original_list)
    all_combinations = []

    # Generate all possible combinations of values within the range 0 to max_value
    # We only care about combinations where each element satisfies the modulo condition
    # We use itertools.product to generate the Cartesian product of possible values
    for combo in itertools.product(range(max_value + 1), repeat=n):
        if (all(combo[i] % n == original_list[i] % n for i in range(n)) and
            sum(combo) == target_sum):
            all_combinations.append(list(combo))

    return all_combinations

def generate_possible_siteswaps(period, balls, max_throw):
    """
    Generate all possible permuations of the list of numbers from 0 to the Max_period
    """
    permutations = [list(perm) for perm in all_permutations([i for i in range(period)])] # Generate all permutations of the list of numbers from 0 to the max_throw
    for perm in permutations:
        perm = [((perm[j] - [i for i in range(period)][j]) % period) for j in range(len(perm))]
        print(perm)
        combinations = expand_siteswap(perm, max_throw, balls * period)
        for combo in combinations:
            print(combo)



if __name__ == '__main__':
    print("Let's generate jugglable siteswap patterns!")
    myPeriod = int(input("Enter the period of the siteswap: "))
    myBalls = int(input("Enter the number of balls: "))
    myMaxThrow = int(input("Enter the maximum throw height: "))
    generate_possible_siteswaps(myPeriod, myBalls, myMaxThrow)

