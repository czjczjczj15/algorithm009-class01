class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # print(prices)
        # max_profit = 0
        
        ### prices.sort()不能用，因为一用了，原来的数据就会被改变
        # nums = prices
        # if prices.sort() == prices:  
        #     return prices[-1] - prices[0]
        # elif prices.sort(reverse = True) == prices:
        #     return max_profit
        # else:
#         original_buy_index = prices[-1]
#         for i in range(len(prices)-1):
#             if (prices[i] - prices[i+1]) < 0:
#                 original_buy_index = i
#                 break

#         if  original_buy_index != prices[-1]:
#             number_of_buy = int( (len(prices)- original_buy_index)/2 )
#             print(number_of_buy)
#             for i in range(number_of_buy):
#                 buy_index = original_buy_index
#                 number_of_possible_sell = len(prices) - buy_index -1
#                 print(number_of_possible_sell)
#                 temp = []
#                 for k in range(i - 1):
#                     print('here')
#                     temp.append(prices[buy_index + 1] - prices[buy_index])
#                     buy_index += 2
#                 for j in range(1,number_of_possible_sell+1):
#                     sell_index = buy_index + j
#                     print('sell',sell_index)
#                     print('buy', buy_index)
#                     temp.append(prices[sell_index] -prices[buy_index] )
#                 if max_profit < sum(temp):
#                     max_profit = sum(temp)
#         return max_profit

        ####################### leedcode python app solution########################
        # return sum([max(prices[i] - prices[i-1], 0) for i in range(1, len(prices))])
        # return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))
        return sum([y - x for x, y in zip(prices[:-1], prices[1:]) if x < y])
                        
        