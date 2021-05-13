def findRestaurant(list1, list2):
    seen = {}
    for i in range(len(list1)):
        try:
            j = list2.index(list1[i])
        except:
            j = -1
        if j >= 0:
            seen[list1[i]] = i + j
    best = min(seen.values())
    for i in seen:
        if seen[i] == best:
            return i


list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]

print(findRestaurant(list1, list2))
print(list('leetcode'))
