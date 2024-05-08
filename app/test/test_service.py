import os


def test_get_rooms_students_count(service):
    service.insert_rooms("input/test_rooms_1.json")
    service.insert_students("input/test_students_1.json")
    items = service.get_rooms_students_count()
    os.remove("rooms_amount.json")
    assert items[0][1] == 4
    assert items[1][1] == 4
    assert items[2][1] == 3


def test_eooms_with_lower_avg_age(service):
    service.insert_rooms("input/test_rooms_2.json")
    service.insert_students("input/test_students_2.json")
    items = service.get_five_rooms_with_least_age_average()

    os.remove("five_rooms_lower_age_average.json")
    list_of_string_items = []
    for i in items:
        list_of_string_items.append("".join(i))
    assert len(items) == 5
    assert "Room #1" in list_of_string_items
    assert "Room #3" in list_of_string_items
    assert "Room #4" in list_of_string_items
    assert "Room #6" in list_of_string_items
    assert "Room #2" in list_of_string_items


def test_amount_rooms_with_diffent_sex(service):
    service.insert_rooms("input/test_rooms_1.json")
    service.insert_students("input/test_students_1.json")
    items = service.get_rooms_with_different_sex()
    os.remove("rooms_with_different_sex.json")
    list_of_string_items = []
    for i in items:
        list_of_string_items.append("".join(i))
    assert len(items) == 2
    assert "Room #1" in list_of_string_items
    assert "Room #3" in list_of_string_items


def test_rooms_with_largest_age_different(service):
    service.insert_rooms("input/test_rooms_2.json")
    service.insert_students("input/test_students_2.json")
    items = service.get_five_rooms_with_largest_age_differnce()
    os.remove("five_rooms_with_largest_age_differnce.json")
    list_of_string_items = []
    for i in items:
        list_of_string_items.append("".join(i))
    assert len(items) == 5
    assert "Room #1" in list_of_string_items
    assert "Room #5" in list_of_string_items
    assert "Room #4" in list_of_string_items
    assert "Room #6" in list_of_string_items
    assert "Room #2" in list_of_string_items
