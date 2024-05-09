import os


def test_get_rooms_students_count(service):
    service.insert_rooms("input/test_rooms_1.json")
    service.insert_students("input/test_students_1.json")
    items = service.get_rooms_students_count("rooms_amount_test.json")
    os.remove("rooms_amount_test.json")
    assert items[0][1] == 4
    assert items[1][1] == 4
    assert items[2][1] == 3


def test_rooms_with_smallest_avg_age(service):
    service.insert_rooms("input/test_rooms_2.json")
    service.insert_students("input/test_students_2.json")
    items = service.get_five_rooms_with_smallest_age_average(
        "five_rooms_smallest_age_average_test.json",
    )
    os.remove("five_rooms_smallest_age_average_test.json")
    list_of_string_items = []
    for i in items:
        list_of_string_items.append("".join(i))
    assert len(items) == 5
    assert "Room #1" in list_of_string_items
    assert "Room #3" in list_of_string_items
    assert "Room #4" in list_of_string_items
    assert "Room #6" in list_of_string_items
    assert "Room #2" in list_of_string_items


def test_amount_rooms_with_mixedSex_students(service):
    service.insert_rooms("input/test_rooms_1.json")
    service.insert_students("input/test_students_1.json")
    items = service.get_rooms_with_mixedSex_students("rooms_with_different_mixed-sex_students_test.json")
    os.remove("rooms_with_different_mixed-sex_students_test.json")
    list_of_string_items = []
    for i in items:
        list_of_string_items.append("".join(i))
    assert len(items) == 2
    assert "Room #1" in list_of_string_items
    assert "Room #3" in list_of_string_items


def test_rooms_with_largest_age_different(service):
    service.insert_rooms("input/test_rooms_2.json")
    service.insert_students("input/test_students_2.json")
    items = service.get_five_rooms_with_largest_age_differnce("five_rooms_with_largest_age_differnce_test.json")
    os.remove("five_rooms_with_largest_age_differnce_test.json")
    list_of_string_items = []
    for i in items:
        list_of_string_items.append("".join(i))
    assert len(items) == 5
    assert "Room #1" in list_of_string_items
    assert "Room #5" in list_of_string_items
    assert "Room #4" in list_of_string_items
    assert "Room #6" in list_of_string_items
    assert "Room #2" in list_of_string_items
