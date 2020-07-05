def reward_function(params):
    '''

    :param params:
    :return: reward(result of behaviour)
    '''

    # var
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    # boolean var
    is_left_of_center = params['is_left_of_center']
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    reward = 0

    if distance_from_center <= marker_1:
        reward += 0.1
    elif distance_from_center <= marker_2:
        reward += 0.5
    elif distance_from_center <= marker_3:
        if is_left_of_center:
            reward += 1.0
        reward += 1.0

    else:
        reward += 1e-3

    return float(reward)
