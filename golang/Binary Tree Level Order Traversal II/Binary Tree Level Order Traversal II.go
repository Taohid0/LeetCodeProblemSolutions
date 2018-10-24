package main

import "fmt"

type TreeNode struct{
	Val int
	Left *TreeNode
	Right *TreeNode
}

func levelOrderBottom(root *TreeNode) [][]int {
	if nil == root {
		return [][]int{}
	}
	treeNodeSlice := make([]*TreeNode,0)
	treeNodeSlice = append(treeNodeSlice, root)
	result := make([][]int,0)


	for len(treeNodeSlice)>0{
		tempList := make([]*TreeNode,0)
		tempResult:=make([]int,0)

		for i:=0;i<=len(treeNodeSlice); i++{
			if treeNodeSlice[i].Left !=nil{
				tempResult = append(tempResult,treeNodeSlice[i].Val)
				tempList = append(tempList, treeNodeSlice[i].Left)
			}
			if treeNodeSlice[i].Right !=nil{
				tempResult = append(tempResult,treeNodeSlice[i].Val)
				tempList = append(tempList, treeNodeSlice[i].Left)
			}

		}

		result = append(result, tempResult)
		treeNodeSlice = tempList



	}
	return result

}

func main()  {
	tree := TreeNode{}
	tree.Left = nil
	tree.Right = nil
	tree.Val = 1
	fmt.Print(levelOrderBottom(&tree))
}

var ret [][]int

func levelTravel(nodeArr []*TreeNode){
	var nextNodeArr []*TreeNode
	var valArr []int

	len1 := len(nodeArr)
	if 0 == len1 {
		return
	}

	for i := 0; i < len1; i++ {
		v := nodeArr[i]
		if nil != v.Left {
			nextNodeArr = append(nextNodeArr, v.Left)
		}
		if nil != v.Right {
			nextNodeArr = append(nextNodeArr, v.Right)
		}

		valArr = append(valArr, v.Val)
	}
	fmt.Printf("valArr:%+v\n", valArr)
	levelTravel(nextNodeArr)

	ret = append(ret, valArr)
}

func levelOrderBottom(root *TreeNode) [][]int {
	if nil == root {
		return [][]int{}
	}
	ret = [][]int{}

	nextNodeArr := []*TreeNode{root}
	levelTravel(nextNodeArr)

	return ret
}

