def sum(arr: list[int]) -> int:
  if len(arr) == 0:
    return 0
  else:
    return arr[0] + sum(arr[1:])


def count_items(arr: list[int]) -> int:
    if len(arr) == 0:
        return 0
    else:
        return 1 + count_items(arr[1:])


def find_max(arr: list[int]) -> int:
    if len(arr) == 0:
        return 0
    else:
        return max(arr[0], find_max(arr[1:]))

def main():
    # test sum
    print(sum([1,4,5,1,3]))
    print(sum([1]))
    print(sum([8,4,5,24,3]))
    print(sum([]))

    # test count items
    print(count_items([1,4,5,1,3]))
    print(count_items([1]))
    print(count_items([8,4,5,24,3]))
    print(count_items([]))

    # test find max
    print(find_max([1,4,5,1,3]))
    print(find_max([1]))
    print(find_max([8,4,5,24,3]))
    print(find_max([]))

if __name__ == "__main__":
    main()
