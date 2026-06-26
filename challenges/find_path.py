from heapq import heappop, heappush

from data_structures.city_map import CityMap


def heuristic(
    city_map: CityMap,
    node: int,
    goal: int,
) -> int:
    return 0


def find_path(
    city_map: CityMap,
    start: int,
    goal: int,
) -> list[int]:

    frontier = []
    heappush(frontier, (0, start))

    came_from = {start: None}
    cost_so_far = {start: 0}

    while frontier:

        _, current = heappop(frontier)

        if current == goal:
            break

        for neighbor in city_map.roads[current]:

            new_cost = cost_so_far[current] + 1

            if (
                neighbor not in cost_so_far
                or new_cost < cost_so_far[neighbor]
            ):

                cost_so_far[neighbor] = new_cost

                priority = (
                    new_cost
                    + heuristic(
                        city_map,
                        neighbor,
                        goal,
                    )
                )

                heappush(
                    frontier,
                    (
                        priority,
                        neighbor,
                    ),
                )

                came_from[neighbor] = current

    if goal not in came_from:
        return []

    path = []

    current = goal

    while current is not None:
        path.append(current)
        current = came_from[current]

    path.reverse()

    return path
