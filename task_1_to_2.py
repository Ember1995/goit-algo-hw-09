import time

def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= coin * count
    return result

def find_min_coins(amount):
    coins = [1, 2, 5, 10, 25, 50]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    result = {}
    current_amount = amount
    while current_amount > 0:
        coin = coin_used[current_amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        current_amount -= coin

    return result

if __name__ == "__main__":
    
    amount = 113

    # Жадібний алгоритм
    start_time = time.time()
    greedy_result = find_coins_greedy(amount)
    greedy_time = time.time() - start_time

    # Алгоритм динамічного програмування
    start_time = time.time()
    dp_result = find_min_coins(amount)
    dp_time = time.time() - start_time

    print("\nТаблиця результатів:")
    print("| Параметр                 | Жадібний алгоритм          | Динамічне програмування    |")
    print("|--------------------------|----------------------------|----------------------------|")
    print(f"| Час виконання (сек)      | {greedy_time:.10f}               | {dp_time:.10f}               |")
    print(f"| Очікуваний результат     | {{50: 2, 10: 1, 2: 1, 1: 1}} | {{1: 1, 2: 1, 10: 1, 50: 2}} |")
    print(f"| Отриманий результат      | {greedy_result} | {dp_result} |")
