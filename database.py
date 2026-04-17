


#################################
### Functions used by the API ###
#################################

def search_db(column_name: str, value) -> list:
    '''Search the course catalog with the given collumn name and value, returns a list of rows.\n
    If an error occurs, return an empty list'''

    # return dummy data for now
    return [
        [123, "test class1", "7:00-8:15", "professor joe"],
        [124, "test class2", "5:00-8:15", "professor bob"],
        [125, "test class3", "15:00-16:15", "professor will"]
        ]


def full_catalog() -> list:
    '''Returns the entire course catalog as a list of rows'''

    # return dummy data
    return [
        [123, "test class1", "7:00-8:15", "professor joe"],
        [124, "test class2", "5:00-8:15", "professor bob"],
        [125, "test class3", "15:00-16:15", "professor will"],
        [126, "test class4", "15:00-16:15", "professor will"],
        [127, "test class5", "15:00-16:15", "professor will"],
        [128, "test class6", "15:00-16:15", "professor will"],
        ]


def add_class(class_data: list) -> tuple[str, int]:
    '''attempt to add a new class to the catalog, returns a tuple of a string response message and an int HTML response code'''

    return ("cannot not add class because function is not implimented.", 500)


def update_class(class_id: int, class_data: list) -> tuple[str, int]:
    '''attempt to update the data for a course, returns a tuple of a string response message and an int HTML response code'''

    return ("cannot not update class because function is not implimented.", 500)