
def knapSack(W, wt, val, n):

    if n == 0 or W == 0:
        return 0
    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1)
    else:
        return max(
            val[n-1] + knapSack(
                W-wt[n-1], wt, val, n-1),
            knapSack(W, wt, val, n-1))
if __name__ == '__main__':
    weight = [int(x) for x in input("Enter weights separated by space: ").split()]
    profit = [int(x) for x in input("Enter values separated by space: ").split()]
    W = int(input("Enter the capacity of knapsack: "))
    n = len(profit)
    print("Max Profit: ", knapSack(W, weight, profit, n) )
    


