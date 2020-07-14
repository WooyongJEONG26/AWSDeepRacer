# needed for calculation for future

# Straight line
def is_straight():
    return 0


# Being right
def is_right(is_left_of_center):
    result = 0
    if is_left_of_center:
        result -= 0.3
    else:
        result += 0.3
    return result


def reward_function(params):
    """
    :param params:  track_width (float)
                    distance_from_center (float)
                    is_left_of_center (boolean)

    :return: reward (float)
    """

    # Read input parameters
    # track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    is_left_of_center = params['is_left_of_center']

    # reward var
    reward = 0

    # Setting range from the center of track
    if 0.0 < distance_from_center <= 0.2:
        reward += is_right(is_left_of_center)
        reward += 0.3
    elif 0.2 <= distance_from_center < 0.6:
        reward += is_right(is_left_of_center)
        reward += 0.4
    else:
        reward = 1e-3  # likely crashed/ close to off track
    return float(reward)
