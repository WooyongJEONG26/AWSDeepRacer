def reward_function(params):
    '''

    :param params: track_width, distance_from_center, is_left_of_center
    :return: reward
    next: got to lets put the agent on the middle of left lane
    '''
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    # boolean var
    is_left_of_center = params['is_left_of_center']
    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # creating reward var to add on from now
    reward = 0

    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        # if distance from center is close to marker and the agent is on the left side
        if is_left_of_center:
            reward += 2.0
        reward += 1.0
    elif distance_from_center <= marker_2:
        reward += 0.5
    elif distance_from_center <= marker_3:
        reward += 0.1
    else:
        reward += 1e-3  # likely crashed/ close to off track

    return float(reward)
