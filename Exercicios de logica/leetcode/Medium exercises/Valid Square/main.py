class Solution:
    def euclidean_distance(self, p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

    def validSquare(self, p1: list[int], p2: list[int], p3: list[int], p4: list[int]) -> bool:
        distances = [
            self.euclidean_distance(p1, p2),
            self.euclidean_distance(p1, p3),
            self.euclidean_distance(p1, p4),
            self.euclidean_distance(p2, p3),
            self.euclidean_distance(p2, p4),
            self.euclidean_distance(p3, p4)
        ]

        distances.sort()

        return distances[0] > 0 and distances[0] == distances[1] == distances[2] == distances[3] and distances[4] == \
            distances[5]