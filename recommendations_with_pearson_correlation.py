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


# pearson correlation formular
# covariance / (standard_deviation_of_x * standard_deviation_of_y)
# covariance = sum((x - x_mean) * (y - y_mean))/n-1 for sample variance
# covariance = sum((x - x_mean) * (y - y_mean))/n for population variance
# standard_deviation_of_x = sqrt(sum(x - x_mean)**2/n)
# standard_deviation_of_y = sqrt(sum(y - y_mean)**2/n)

# pearson correlation = sum_of_products_of_x_and_y - (sum_of_x * sum_of_y) / sqrt((sum_of_squares_of_x - square_of_sum_of_x)(sum_of_squares_of_y - square_of_sum_of_y))


def findSimilarityScore(preferences, person1, person2):
    commonMovies = {}
    for movie in preferences[person1]:
        if movie in preferences[person2]:
            commonMovies[movie] = 1

    # print(commonMovies)

    person1Sum = 0
    person2Sum = 0
    person1SquareSum = 0
    person2SquareSum = 0
    productSum = 0

    n = len(commonMovies)

    if n == 0:
        return 0

    for movie in commonMovies:
        # build sum of products of x and y.
        person1Rating = preferences[person1][movie]
        person2Rating = preferences[person2][movie]

        # print(person1 + "'s rating for movie " +
        #       movie + " is : ", person1Rating)
        # print(person2 + "'s rating for movie " +
        #       movie + " is : ", person2Rating)
        person1Sum = person1Sum + person1Rating
        person2Sum = person2Sum + person2Rating
        person1SquareSum = person1SquareSum + pow(person1Rating, 2)
        person2SquareSum = person2SquareSum + pow(person2Rating, 2)
        productSum = productSum + (person1Rating * person2Rating)

    covariance = productSum - (person1Sum * person2Sum)/n
    standardDeviation = sqrt(
        (person1SquareSum - pow(person1Sum, 2)/n) * (person2SquareSum - pow(person2Sum, 2)/n))

    if standardDeviation == 0:
        return 0

    return covariance/standardDeviation


# similarityScore = findSimilarityScore(critics, 'Lisa Rose', 'Gene Seymour')

# print('Score is: ', similarityScore)


def findMatches(preferences, person, matchCount):
    scores = [(findSimilarityScore(preferences, person, other), other)
              for other in preferences if other != person]

    scores.sort()
    scores.reverse()
    return scores[0:matchCount]


def recommendMovies(preferences, person):
    simTotals = {}
    weightedScore = {}
    recommendedMovies = []

    for eachPerson in preferences:
        if eachPerson != person:
            simScore = findSimilarityScore(preferences, person, eachPerson)

            if simScore <= 0:
                continue

            for movie in preferences[eachPerson]:
                if movie not in preferences[person] or preferences[person][movie] == 0:
                    simTotals.setdefault(movie, 0)
                    simTotals[movie] = simTotals[movie] + simScore
                    weightedScore.setdefault(movie, 0)
                    weightedScore[movie] = weightedScore[movie] + \
                        (simScore * preferences[eachPerson][movie])

    # print(simTotals)
    # print(weightedScore)

    for movie in weightedScore:
        recommendedMovies.append(
            (movie, weightedScore[movie]/simTotals[movie]))

    recommendedMovies.sort()
    recommendedMovies.reverse()

    return recommendedMovies


print(recommendMovies(critics, 'Toby'))
# matches = findMatches(critics, 'Toby', 3)
# print(matches)


# print(critics)
# print(critics['Toby'])
# recommendMovies(critics, 'Toby')
