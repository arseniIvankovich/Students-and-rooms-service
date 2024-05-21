import os


def test_get_rooms_students_count(service):
    service.insert_rooms("input/test_rooms_1.json")
    service.insert_students("input/test_students_1.json")
    items = service.get_rooms_students_count_json("rooms_amount_test.json")
    os.remove("rooms_amount_test.json")
    errors = []
    if not items[0][1] == 4:
        errors.append("in the first incorrect amount")
    if not items[1][1] == 4:
        errors.append("in the second incorrect amount")
    if not items[1][1] == 4:
        errors.append("in the third incorrect amount")
    assert not errors, "errors occured:\n{}".format("\n".join(errors))


def test_rooms_with_smallest_avg_age(service):
    service.insert_rooms("input/test_rooms_2.json")
    service.insert_students("input/test_students_2.json")
    items = service.get_five_rooms_with_smallest_age_average_json(
        "five_rooms_smallest_age_average_test.json",
    )
    os.remove("five_rooms_smallest_age_average_test.json")
    list_of_string_items = []
    for i in items:
        list_of_string_items.append("".join(i))
    errors = []
    if not len(items) == 5:
        errors.append("incorrect length")
    if not "Room #1" in list_of_string_items:
        errors.append("Room #1 not in list")
    if not "Room #3" in list_of_string_items:
        errors.append("Room #3 not in list")
    if not "Room #4" in list_of_string_items:
        errors.append("Room #4 not in list")
    if not "Room #6" in list_of_string_items:
        errors.append("Room #6 not in list")
    assert not errors, "errors occured:\n{}".format("\n".join(errors))


def test_amount_rooms_with_mixedSex_students(service):
    service.insert_rooms("input/test_rooms_1.json")
    service.insert_students("input/test_students_1.json")
    items = service.get_rooms_with_mixedSex_students_json("rooms_with_different_mixed-sex_students_test.json")
    os.remove("rooms_with_different_mixed-sex_students_test.json")
    list_of_string_items = []
    for i in items:
        list_of_string_items.append("".join(i))

    errors = []
    if not len(items) == 2:
        errors.append("incorrect length")
    if not "Room #1" in list_of_string_items:
        errors.append("Room #1 not in list")
    if not "Room #3" in list_of_string_items:
        errors.append("Room #3 not in list")

    assert not errors, "errors occured:\n{}".format("\n".join(errors))


def test_rooms_with_largest_age_different(service):
    service.insert_rooms("input/test_rooms_2.json")
    service.insert_students("input/test_students_2.json")
    items = service.get_five_rooms_with_largest_age_differnce_json("five_rooms_with_largest_age_differnce_test.json")
    os.remove("five_rooms_with_largest_age_differnce_test.json")
    list_of_string_items = []
    for i in items:
        list_of_string_items.append("".join(i))
    errors = []
    if not len(items) == 5:
        errors.append("incorrect length")
    if not "Room #1" in list_of_string_items:
        errors.append("Room #1 not in list")
    if not "Room #5" in list_of_string_items:
        errors.append("Room #5 not in list")
    if not "Room #6" in list_of_string_items:
        errors.append("Room #6 not in list")
    assert not errors, "errors occured:\n{}".format("\n".join(errors))
