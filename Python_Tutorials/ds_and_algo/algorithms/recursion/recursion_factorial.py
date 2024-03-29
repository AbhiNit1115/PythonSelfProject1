# How to write recursion in 3 steps
# Step 1: Recursive Case     --> The flow
# Step 2: Base case          --> The stopping criteria
# Step 3: Unintentional case --> the constraint --> Identifies the constraints in the code for this case the
# number must be a positive integer

def factorial(n):
    assert n >= 0 and int(n) == n, "The number must be positive integer"
    if n < 1:
        return 1
    else:
        return n * factorial(n - 1)


f = factorial(5)
print(f)