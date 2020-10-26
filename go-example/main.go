package main

import (
	"fmt"
)

func main() {
	testSimple()
}

func testSimple() {
	sm := simple_example.SimpleMessage {
		Id: 1234,
		IsSimple: true,
		Name: "Simple message",
		SampleList: []int32: {10,12},
	}
	fmt.Println(sm)

}
