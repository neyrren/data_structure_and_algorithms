def sum_even_numbers(my_list):
    return sum(x for x in my_list if x % 2 == 0)

if __name__ == "__main__":
    print(sum_even_numbers([1, 2, 3, 4, 5, 6]))
