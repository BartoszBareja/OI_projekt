# Least Recently Used

from imports import *


def check_if_value_exists(value, array):
    for i in array:
        if i["number"] == int(value):
            return i
    return False


data = import_replacement_data()

page_frame_numbers = 3

for page_set in data:
    pages = []
    page_failures = 0
    for i in page_set:
        print(pages)
        if len(pages) < page_frame_numbers and not check_if_value_exists(i, pages):
            pages.append({"number": int(i), "last_used": 0})
            page_failures += 1
        else:

            value = check_if_value_exists(i, pages)

            if value == False:
                page_failures += 1

                max_time = max(pages, key=lambda x: x["last_used"])

                for j in range(len(pages)):
                    if pages[j] == max_time:
                        pages[j] = {"number": int(i), "last_used": 0}

            else:
                for j in range(len(pages)):
                    if pages[j] == value:
                        pages[j]["last_used"] = 0

        for i in pages:
            i["last_used"] = int(i["last_used"]) + 1

    print(f"page failures: {page_failures}")
