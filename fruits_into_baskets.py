def fruits_into_baskets(fruits):
    fruit_frequency = {}
#['A', 'B', 'C', 'A', 'C']
    for window_end in range(0,len(fruits)):
        right_fruit = fruits[window_end]
        if right_fruit not in fruit_frequency:
            fruit_frequiency[right_fruit] = 0
        fruit_frequency[right_fruit] += 1

