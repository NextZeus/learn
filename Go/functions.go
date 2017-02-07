package main

import "fmt"

//func add(x int, y init) int {
//    return x + y
//}

//连续相同类型变量 可简写
func add(x, y int) int {
	return x + y
}

//多值返回
func swap(x, y string) (string, string){
	return y, x
}

//命名返回值
func split(sum int) (x, y int)  {
	x = sum * 4 / 9
	y = sum - x
	return
}

func main(){
    	fmt.Println(add(42, 13))
	a, b := swap("hello", "world")
	fmt.Println(a, b)
	fmt.Println(split(17))
}