"""
Question:
Maximum Units on a Truck
https://leetcode.com/problems/maximum-units-on-a-truck/

"""

from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # sort boxTypes list
        # sorting is O(n log n)
        boxTypes.sort(key=lambda b:b[1], reverse=True)
        
        # calculate the max units
        maximumUnits = 0
        # For loop is O(n)
        for i in range(len(boxTypes)):
            if truckSize >= boxTypes[i][0]:
                boxes = boxTypes[i][0]
                truckSize -= boxTypes[i][0]
            elif truckSize <= 0:
                break
            else:
                boxes = truckSize
                truckSize -= boxTypes[i][0]
            
            maximumUnits += boxes * boxTypes[i][1]
            
        return maximumUnits


class Solution2:
    """
    Refer to https://leetcode.com/problems/maximum-units-on-a-truck/discuss/2220452/PythonC%2B%2B-Simple-and-Intuitive-Greedy-Explanation
    """
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # sort boxTypes list
        # sorting is O(n log n)
        boxTypes.sort(key=lambda b:b[1], reverse=True)
        
        # calculate the max units
        maximumUnits = 0
        # For loop is O(n)
        for box_num, unit_num in boxTypes:
            boxes = min(truckSize, box_num)
            maximumUnits += boxes * unit_num
            truckSize -= boxes
            
        return maximumUnits

def test_maximumUnits():
    s = Solution()
    boxTypes = [[3,1], [1,3],[2,2]]
    truckSize = 4
    assert s.maximumUnits(boxTypes, truckSize) == 8
    boxTypes = [[5,10],[2,5],[4,7],[3,9]]
    truckSize = 10
    assert s.maximumUnits(boxTypes, truckSize) == 91


if __name__ == "__main__":
    test_maximumUnits()