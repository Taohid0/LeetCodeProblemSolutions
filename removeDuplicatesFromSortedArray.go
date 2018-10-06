package main

import "fmt"

func removeDuplicates(nums []int) int {
	if len(nums)<=1{
		return len(nums)
	}
	for i:=1;i<len(nums);i++{
		if (nums[i]==nums[i-1]) {
			nums = append(nums[:i],nums[i+1:len(nums)]...)
			i = i-1
		}
	}
	return len(nums)
}


func main() {
	arr :=[]int{1,3,4,4}
	fmt.Print(removeDuplicates(arr))
}