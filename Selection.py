
def findSmallest(arr):
	#储存数组第一个值为最小值
	smallest = arr[0]
	#储存最小值的索引
	smallest_index = 0
	#循环，查找最小值
	for i in range(1, len(arr)):
		if arr[i] < smallest:
			#如果数组里的值小于最小值，就把这个值赋值给最小值
			smallest = arr[i]
			#给最小值的索引赋值
			smallest_index = i
	#返回最小值的索引
	return smallest_index

#数组排序方法，对数组进行排序
def selectionSort(arr):
	#创建一个新数组，用作整理后输出
	newArr = []
	#遍历数组
	for i in range(len(arr)):
		#调用findSmallest方法,把最小值放进数组
		smallest = findSmallest(arr)
		#把arr的最小值赋值给newArr，pop方法是把数组的数据输出并删除
		newArr.append(arr.pop(smallest)) #arr.pop(smallest)中的smallest是arr数组的索引
	#输出新数组
	return newArr

test_arr = [50,7,9,20,54,30,25,15,75,43]

test = selectionSort(test_arr)

print(test)
