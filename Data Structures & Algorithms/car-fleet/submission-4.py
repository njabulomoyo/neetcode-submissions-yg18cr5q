class Solution:
    """
    Understand:
        so the cars are in different positions, travellig at different speeds
        we have to rearrange the cars accoding to their positions, sort()

    Plan:
        1. rearrange the positions o the cars
        2. put the positions and the speed together
        3. iterate thru the list 
        4. check if the car we are at will arrive at the desyination earlier or later than the car ahead
        5 if it arrives early, contiue, check the next time
        6. otherwise add new fleet
        7. do it for all cars
    """
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        curr = 0
        fleet = 0
        #[(0.1),(1,2),(4,2),(7,1)]
        for pos, spd in sorted(zip(position,speed), reverse=True):
            eta = (target - pos)/spd
            print(eta)
            if eta > curr:
                fleet += 1
                curr = eta

        return fleet
            


















