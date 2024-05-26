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

# Тестування
if __name__ == "__main__":

    # Задана умовами задачі сума
    amount = 113

    # Жадібний алгоритм
    start_time_1 = time.time()
    greedy_result_1 = find_coins_greedy(amount)
    greedy_time_1 = time.time() - start_time_1

    # Алгоритм динамічного програмування
    start_time_1 = time.time()
    dp_result_1 = find_min_coins(amount)
    dp_time_1 = time.time() - start_time_1

    print("\nПеревірка результату: ")
    print("| Параметр                  | Жадібний алгоритм          | Динамічне програмування      |")
    print("|---------------------------|----------------------------|------------------------------|")
    print(f"| Очікуваний результат      | {{50: 2, 10: 1, 2: 1, 1: 1}} | {{1: 1, 2: 1, 10: 1, 50: 2}}   |")
    print(f"| Отриманий результат       | {greedy_result_1} | {dp_result_1}   |")

    # Збільшуємо суму
    amount = 1113

    # Жадібний алгоритм
    start_time_2 = time.time()
    greedy_result_2 = find_coins_greedy(amount)
    greedy_time_2 = time.time() - start_time_2

    # Алгоритм динамічного програмування
    start_time_2 = time.time()
    dp_result_2 = find_min_coins(amount)
    dp_time_2 = time.time() - start_time_2

    print("\nТестування різних сум:")
    print("| Сума                      | Жадібний алгоритм, сек     | Динамічне програмування, сек |")
    print("|---------------------------|----------------------------|------------------------------|")
    print(f"| 113                       | {greedy_time_1:.10f}               | {dp_time_1:.10f}                 |")
    print(f"| 1113                      | {greedy_time_2:.10f}               | {dp_time_2:.10f}                 |")