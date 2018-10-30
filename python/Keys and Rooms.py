class Solution:
    def canVisitAllRooms(self, rooms):
        visited = [0 for i in range(1000)]
        visited[0] = 1
        nodes = [0]

        while nodes:
            temp_nodes = []
            for i in nodes:
                for j in rooms[i]:
                    if not visited[j]:
                        visited[j] = 1
                        temp_nodes.append(j)
            nodes = temp_nodes
        return all(visited[:len(rooms)])
