package main

func twoSum(nums []int, target int) []int {
	counterMap := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		counterMap[nums[i]] = i
	}
	for i := 0; i < len(nums); i++ {
		remaining_value := target - nums[i]
		_, exists := counterMap[remaining_value]
		if (exists && i!=counterMap[remaining_value]) {
			return []int{i, counterMap[remaining_value]}
		}
	}
	return nil;
}

func main() {
	print(twoSum([]int{3, 2, 4}, 6))
}
