mountain_in_japan = {'fuji': 3776, 'kitadake': 3193,
                    'okuhodakadake': 3190, 'dummy': 0}
mountain_in_japan_sorted = sorted(mountain_in_japan.items(),
                                  key=lambda x: x[1], reverse=True)
print(mountain_in_japan_sorted)

mountain_in_japan_dict_items = mountain_in_japan.items()
print(sorted(mountain_in_japan_dict_items, key=lambda x: x[1]))

