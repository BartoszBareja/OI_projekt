# Most Frequently Used

# function to check if a value of given number exists in array
def check_if_value_exists(value, array):
    for i in array:
        if i["number"] == int(value):
            return i
    return False


# declaring function to use MFU
def most_frequently_used(data, capacity):
    print(f"Now using Most Frequently Used with capacity: {capacity}")
    print("-" * 40)
    tests = 1

    # iterating through different data sets
    for data_set in data:

        # declaring pagging errors numbers and array of pages
        paging_errors = 0
        pages = []

        # iterating through different page numbers
        for i in data_set:


            # if there is page to be loaded which already isn't in array, add page and increase paging errors number
            if len(pages) < capacity and not check_if_value_exists(i, pages):
                pages.append({"number": int(i), "times_used": 1})
                paging_errors += 1

            else:

                # if there is no space in array and next page is already in array, increase the number of times the page has been used
                if check_if_value_exists(i, pages):
                    # for loop to find existing value and increment "times_used"
                    for j in range(len(pages)):
                        if pages[j]["number"] == i:
                            pages[j]["times_used"] += 1

                # if there is no space in array and next page is not already in array, swap the most used page with next to be loaded
                else:
                    # find most used page, and increase number of paging error
                    max_used = max(pages, key=lambda x: x["times_used"])
                    paging_errors += 1
                    # for loop for finding most used page and swapping it
                    for j in range(len(pages)):
                        if pages[j] == max_used:
                            pages[j] = {"number": int(i), "times_used": 1}

        print(f"Test number: {tests}")
        print(f"Number of pagigng errors: {paging_errors}")
        tests += 1
