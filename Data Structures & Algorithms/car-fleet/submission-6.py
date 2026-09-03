class Solution:
    """
    position/speed, time
    with time, we determine our fleet numbers
    initiate a variable to store the time of the last fleet
    """
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = [(p,s) for p, s in zip(position, speed)]
        track = 0
        count = 0
        for elem in sorted(cars,reverse=True):
            pos, spd = elem
            time = (target-pos)/spd
            if time > track:
                count += 1
                track = time
        return count

        