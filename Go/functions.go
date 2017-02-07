package main

import "fmt"
import (
	"math/cmplx"
)


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

//变量声明
var c, python, java bool = true, false, true

func main(){
    	fmt.Println(add(42, 13))
	a, b := swap("hello", "world")
	fmt.Println(a, b)
	fmt.Println(split(17))

	// := 不能使用在函数外 常量不能使用:=定义
	c, python, java  := true, false, true

	var i int = 0
	fmt.Print(i, c , python, java)

	var (
		ToBe bool = false
		MaxInt uint64 = 1<<64 - 1
		z complex128 = cmplx.Sqrt(-5 + 12i)
	)

	const f = "%T(%v)\n"
	fmt.Printf(f, ToBe, ToBe)
	fmt.Printf(f, MaxInt, MaxInt)
	fmt.Printf(f, z, z)

	//零值 0 false ""

	//类型转换
	m := 42
	fl := float64(m)
	u := uint(fl)
	fmt.Print('u', u)

}