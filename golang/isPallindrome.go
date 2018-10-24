package main
func reverse(x int)  int{
	var result = 0
	for x != 0 {
		result = (x%10)+result *10
		x/=10
	}
	return result
}
func isPalindrome(x int) bool {
	if x<0{
		return false
	}
	return x==reverse(x)
}
