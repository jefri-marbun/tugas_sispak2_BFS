
def main():  

        #     0  1  2  3
        #  0  0  1  1  0
        #  1  0  0  1  0
        #  2  1  0  0  1
        #  3  0  0  0  1

        # graph dalam bentuk matrix
	matrix = [[0,1,1,0],
                  [0,0,1,0],
                  [1,0,0,1],
                  [0,0,0,1]];

	# Array
	visited = [0,0,0,0]

	# tambahkan node 
	# Node 0 sebagai awal
	queue = [0]

	# tentukan value node
	visited[0] = 1

	# Dequeue node 0
	node = queue.pop(0);
	print node

	while True:

		for x in range (0, len(visited)):

                        
			if matrix[node][x] == 1 and visited[x] == 0:

                                # Visit node
				visited[x] = 1;

                                # Enqueue element
				queue.append(x)

		# saat queue kosong, lakukan break		
		if len(queue) == 0:
			break;

		else:

                        # deque element dari queue
			node = queue.pop(0)
			print node
	
if __name__ == "__main__":
	main()
