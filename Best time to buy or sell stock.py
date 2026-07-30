prices = [7,1,5,3,6,4]

# Brute Force Approach 
profit=0
n=len(prices)
for i in range(0,n-1):
    for j in range(i+1,n):
        profit=max(profit,prices[j]-prices[i])

print(profit)
# Time Complexity is O(N²) and space complexity is O(1)   

# Optimal Approache
def maxProfit( prices):
       n=len(prices)
       maxprofit=0
       minvalue=float("inf")
       for i in range(0,n):

        minvalue=min(minvalue,prices[i])
        maxprofit=max(maxprofit,prices[i]-minvalue)
       return maxprofit
            
print(maxProfit(prices))
# Time Complexity is O(N) and space complexity is O(1)  
    



    
