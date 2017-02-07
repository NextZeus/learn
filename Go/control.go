package main

import (
	"fmt"
	"runtime"
)

func main()  {
	sum := 0
	for i:=0; i< 10; i++ {
		sum += i
	}
	fmt.Println(sum)

	//while
	sum1 := 1
	for sum1 < 1000{
		sum1+=sum1
	}

	//if
	a:=0
	if a<=0{
		fmt.Println("a <= 0")
	}

	switch os:=runtime.GOOS;os {
	case "darwin":
		fmt.Println("OS X.")
	case "linux":
		fmt.Println("Linux.")
	default:
		fmt.Printf("%s.", os)
	}
}