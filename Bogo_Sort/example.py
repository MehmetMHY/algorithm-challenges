from module import bs

print("BOGOSORT() - EXAMPLE OUTPUT")
test_list = [2, 4, 3, 1, 99, 1, 9]
sorted_list, attempts, time = bs.bogosort(test_list, True, False)
print("Sorted List: ", sorted_list)
print("Attemps/Steps:", attempts)
print("Runtime:", str(time) + " sec")

print()

print("BOGOEXAMPLE() - EXAMPLE OUTPUT")
bs.bogoExample(3)

