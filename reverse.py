num = input("Enter comma-separated numbers: ")

num_list = [int(i.strip()) for i in num.split(',') if i.strip()]

if len(num_list) > 0:
    num_tuple = tuple(num_list)

    print("List :", num_list)
    print("Tuple :", num_tuple)
    print("Total number of elements:", len(num_list))
    print("First element:", num_list[0])
    print("Last element:", num_list[-1])  # Negative indexing - counts backward
    print("List in reverse order:", num_list[::-1])  # [start:stop:step]
else:
    print("Please enter at least one number.")