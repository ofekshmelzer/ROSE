from rose.common import obstacles, actions  # NOQA

driver_name = "Stern"


def obstacle(world, x, y):
    try:
        obstacle = world.get((x, y))
    except IndexError:
        # x, y - 1 is not a valid position
        return False
    else:
        return obstacle

    return False


def harm_obstacle(world, x, y):
    try:
        obstacle = world.get((x, y))
    except IndexError:
        # x, y - 1 is not a valid position
        return False
    else:
        if obstacle == obstacles.TRASH or obstacle == obstacles.BIKE or obstacle == obstacles.BARRIER:
            return True


def penguin(world, x, y):
    try:
        obstacle = world.get((x, y))
    except IndexError:
        # x, y - 1 is not a valid position
        return False
    else:
        if obstacle == obstacles.PENGUIN:
            return True


def drive(world):
    x = world.car.x
    y = world.car.y
    # print('x value is ' + str(x))
    # print('y value is ' + str(y))
    # print('omer is a ' + FrontObstacle

    # Choose the best action for obstacle
    if penguin(world, x, y - 1):
        return actions.PICKUP

    elif penguin(world, x + 1, y - 2) and x != 2 and not harm_obstacle(world, x + 1, y - 1):

        return actions.RIGHT
    elif penguin(world, x - 1, y - 2) and x != 3 and not harm_obstacle(world, x - 1, y - 1):
        return actions.LEFT

    else:
        if obstacle(world, x, y - 1) == obstacles.CRACK:
            return actions.JUMP
        if (not penguin(world, x - 1, y - 3) or not harm_obstacle(world, x, y - 1) or not harm_obstacle(world, x - 1,
                                                                                                        y - 2)) and obstacle(
            world, x + 1, y - 2) == obstacles.CRACK and x != 2 and not harm_obstacle(world, x + 1, y - 1):
            return actions.RIGHT
        if (not penguin(world, x + 1, y - 3) or harm_obstacle(world, x, y - 1) or harm_obstacle(world, x + 1,
                                                                                                        y - 2)) and obstacle(
            world, x - 1, y - 2) == obstacles.CRACK and x != 3 and not harm_obstacle(world, x, y - 1):
            return actions.LEFT

        else:
            if obstacle(world, x, y - 1) == obstacles.WATER:
                return actions.BRAKE
            if (not penguin(world, x - 1, y - 3) or not harm_obstacle(world, x, y - 1) or not harm_obstacle(world,
                                                                                                            x - 1,
                                                                                                            y - 2)) and obstacle(
                world, x + 1, y - 2) == obstacles.WATER and x != 2 and not harm_obstacle(world, x + 1, y - 1):
                return actions.RIGHT
            if (not penguin(world, x + 1, y - 3) or harm_obstacle(world, x, y - 1) or harm_obstacle(world, x + 1,
                                                                                                    y - 2)) and obstacle(
                world, x - 1, y - 2) == obstacles.WATER and x != 3 and not harm_obstacle(world, x, y - 1):
                return actions.LEFT

    # car1 lane
    if x == 0:
        action = actions.RIGHT
    elif x == 2:
        action = actions.LEFT
    elif x == 1:
        action = actions.RIGHT

    # car2 lane
    if x == 3:
        action = actions.RIGHT
    elif x == 5:
        action = actions.LEFT
    elif x == 4:
        action = actions.LEFT

    FrontObstacle = world.get((x, y - 1))

    if FrontObstacle == obstacles.NONE and penguin(world, x, y - 2) == False:
        if obstacle(world, 1, y - 1) == obstacles.NONE or obstacle(world, 1, y - 1) == obstacles.WATER or obstacle(
                world, 1, y - 1) == obstacles.CRACK:
            if x == 0:
                return actions.RIGHT
            elif x == 2:
                return actions.LEFT
        elif obstacle(world, 4, y - 1) == obstacles.NONE or obstacle(world, 4, y - 1) == obstacles.WATER or obstacle(
                world, 4, y - 1) == obstacles.CRACK:
            if x == 3:
                return actions.LEFT
            elif x == 5:
                return actions.RIGHT

        return actions.NONE

    elif FrontObstacle == obstacles.TRASH:
        return action
    elif FrontObstacle == obstacles.CRACK:
        return actions.JUMP
    elif FrontObstacle == obstacles.WATER:
        return actions.BRAKE
    elif FrontObstacle == obstacles.BIKE:
        return action
    elif FrontObstacle == obstacles.BARRIER:
        return action

    return actions.NONE