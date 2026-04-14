class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        boxes = {}      
        for ball_number in range(lowLimit, highLimit + 1):
            box_id = 0
            temp = ball_number
            while temp > 0:
                box_id += temp % 10
                temp //= 10
            if box_id in boxes:
                boxes[box_id] += 1
            else:
                boxes[box_id] = 1
        return max(boxes.values())