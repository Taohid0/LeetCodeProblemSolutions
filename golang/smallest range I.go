package main

func maxInt(nums []int) int{
	maximumValue := nums[0]
	for _,value := range nums{
		if value>maximumValue{
			maximumValue = value
		}
	}
	return maximumValue
}

func minInt(nums []int) int{
	minimumValue := nums[0]
	for _,value := range nums{
		if value<minimumValue{
			minimumValue = value
		}
	}
	return minimumValue
}

func smallestRangeI(A []int, K int) int {
	maximum_value := maxInt(A)
	minimum_value := minInt(A)

	difference  := maximum_value-minimum_value
	difference-= K*2
	return difference


}
