package main

func longestCommonPrefix(strs []string) string {
	if len(strs) >= 1 {
		result := strs[0]
		for I := 1; I < len(strs); I++ {
			if len(strs[I]) < len(result) {
				result = result[:len(strs[I])]  //tricky :P
			}
			for  J:= 0; J < len(result); J++ {
				if result[J] != strs[I][J] {
					result = result[:J]
					break //not so tricky :P 
				}
			}
		}
		return result
	}
	return ""
}

func main() {
	longestCommonPrefix([]string{""})
}
