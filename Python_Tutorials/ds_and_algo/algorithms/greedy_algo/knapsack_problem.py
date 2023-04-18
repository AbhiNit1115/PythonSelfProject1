class Items:

    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight


def knapsack_method(items, capacity):
    # first sort the items based on their ration
    items.sort(key=lambda x: x.ratio, reverse=True)
    used_capacity = 0
    total_value = 0
    for i in items:
        if used_capacity + i.weight < capacity:
            used_capacity += i.weight
            total_value += i.value
        else:
            unused_weight = capacity - used_capacity
            value = i.ratio * unused_weight
            used_capacity += unused_weight
            total_value += value
        if used_capacity == capacity:
            break
    print("Total value obtained: "+str(total_value))


item1 = Items(20, 100)
itetm2 = Items(30, 120)
itetm3 = Items(10, 60)
cList = [item1, itetm2, itetm3]
knapsack_method(cList, 50)
