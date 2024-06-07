# Least Recently Used

from imports import *


# function to check if page with given number exists in array
def check_if_value_exists(value, array):
    for i in array:
        if i["number"] == int(value):
            return i
    return False


def least_recently_used(data, capacity):
    print(f"Now using Least Recently Used with capacity: {capacity}")
    print("-" * 40)

    test = 1
        # declaring variable to store the size of page buffer
    page_frame_numbers = capacity

    # iterating through sets of pages from given data
    for page_set in data:

        # declaring buffer to store pages
        pages = []

        # declaring variable to store number of page faults
        page_failures = 0

        # iterating through pages in page set
        for i in page_set:

            # if there is free space in buffer, and given value is not yet in buffer
            if len(pages) < page_frame_numbers and not check_if_value_exists(i, pages):
                pages.append({"number": int(i), "last_used": 0})
                page_failures += 1
            else:

                # variable to store and check whether given value is present in buffer
                value = check_if_value_exists(i, pages)

                # if given page is not yet in buffer
                if not value:
                    page_failures += 1

                    # outputting page with the highest value of "last_used"
                    max_time = max(pages, key=lambda x: x["last_used"])

                    # swapping page with the highest "last_used" with freshly input page
                    for j in range(len(pages)):
                        if pages[j] == max_time:
                            pages[j] = {"number": int(i), "last_used": 0}

                # if given page is in buufer
                else:
                    # finding page with the same number as given, and updating the last time it was used
                    for j in range(len(pages)):
                        if pages[j] == value:
                            pages[j]["last_used"] = 0

            # at the end of each load of page, increase each page size by 1
            for i in pages:
                i["last_used"] = int(i["last_used"]) + 1

        # outputting final value of page failures
        print(f"Test number: {test}")
        print(f"page failures: {page_failures}")
        test += 1
