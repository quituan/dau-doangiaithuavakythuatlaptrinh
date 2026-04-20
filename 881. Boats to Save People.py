class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        
        light = 0
        heavy = len(people) - 1
        boats = 0
        
        while light <= heavy:
            if people[light] + people[heavy] <= limit:
                light += 1
            
            heavy -= 1
            
            boats += 1
            
        return boats