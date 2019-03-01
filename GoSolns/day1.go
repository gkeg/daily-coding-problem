/*

Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
*/

package main

import "fmt"

func twoSum(arr []int, k int) bool {
	complements := make(map[int]bool)
	n := len(arr)
	for i := 0; i < n; i++ {
		cur_elem := arr[i]
		if _, ok := complements[cur_elem]; ok {
			return true	
		} else {
			complements[k-cur_elem] = true
		}
	}
	return false
}

func main() {
	arr := [3]int{4, 5, 6}
	arr2 := [5]int{4, 2, 6, 3, 9}

	// False
	fmt.Println(twoSum(arr[:], 3))

	// True
	fmt.Println(twoSum(arr2[:], 10))
}
