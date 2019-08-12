from math import sqrt

# A dictionary of movie critics and their ratings of a small
# set of movies
critics = {'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
                         'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
                         'The Night Listener': 3.0},
           'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
                            'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
                            'You, Me and Dupree': 3.5},
           'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
                                'Superman Returns': 3.5, 'The Night Listener': 4.0},
           'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
                            'The Night Listener': 4.5, 'Superman Returns': 4.0,
                            'You, Me and Dupree': 2.5},
           'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
                            'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
                            'You, Me and Dupree': 2.0},
           'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
                             'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
           'Toby': {'Snakes on a Plane': 4.5, 'You, Me and Dupree': 1.0, 'Superman Returns': 4.0}}


def similarity_score(preferences, person_1, person_2):
    similar_items = {}

    for item in preferences[person_1]:
        if item in preferences[person_2]:
            similar_items[item] = 1

    if len(similar_items) == 0:
        return 0

    # print(similar_items)

    # sum_of_squares = sum([(pow((preferences[person_1][item] - preferences[person_2][item]), 2)) for item in preferences[person_1] if item in preferences[person_2]])
    sum_of_squares = 0

    # for item in preferences[person_1]:
    #     if item in preferences[person_2]:
    #         square_value = pow(
    #             (preferences[person_1][item] - preferences[person_2][item]), 2)
    #         sum_of_squares = sum_of_squares + square_value

    # square_root_value = sum_of_squares

    # return 1/(1 + square_root_value)

    for item in similar_items:
        first_person_rating = preferences[person_1][item]
        second_person_rating = preferences[person_2][item]

        # print('Movie name: ' + item)
        # print(person_1 + "'s rating: ",  first_person_rating)
        # print(person_2 + "'s rating: ",  second_person_rating)

        difference = first_person_rating - second_person_rating

        # print('difference: ', difference)

        square_value = pow(difference, 2)

        # print('squared value: ', square_value)
        sum_of_squares = sum_of_squares + square_value

    return 1/(1 + sqrt(sum_of_squares))
