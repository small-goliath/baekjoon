/*
[Snippets]

# General

vv			initialize variable varName := value
ier			if error if err != nil { myStatements }
ifok		if ok if value,ok := myFunc; ok { myStatements }
fr			for range for _, v := range values { myStatements }
frr			for range channel for v := range channel { myStatements }
def			case default default:
cl			close close(closable)
fms			fmt Sprintf fmt.Sprintf("%+v", args)
fme			fmt Errorf fmt.Errorf("%+v", args)
ctx			ctx context.Context

# Types

st			struct type
type structName struct {
}
sf			struct field fieldName string
stt			struct tag `json:"jsonFieldName"`
ne			struct constructor method

	func NewFoo() *Foo{
		return &Foo {
		}
	}

inte			Interface type
type interfaceName interface {
}

# Collection manipulation
sr			remove one element from slice slice = append(slice[:index], slice[index+1:]...)
ap			append element to slice slice = append(slice, element)
del			delete map element by key delete(map, key)

# Return values
rn			Return Nil return nil
rne			Return Nil and err return nil, err
re			Return err return err
Logging
lo			log variable log.Printf("%+v\n", varName)
le			log error log.Printf("%+v\n", err)
lef			log error (when using logrus) log.Errorf("%+v\n", err)
lf			log fatal log.Fatal(err)
lff			log fatal log.Fatalf("%+v\n", err)

# Error Handling
es			errors with stack errors.WithStack(err)
em			error with message errors.WithMessage(err, message)
emf			error with messagef errors.WithMessagef(err, format, args)
is			errors Is if errors.Is(err, MyError) { myStatements }
as			errors As
var e ErrorType

	errors.As(err, &e) {
		myStatements
	}

# Concurrency
gofunc			anonymous go function go func() { myStatements }
defunc			anonymous defer function defer func { myStatements }
lock			sync.Mutex Lock and defer Unlock
mu.Lock()
defer mu.Unlock()
nb				non-blocking channel send
select {
case msg <- msgChan:
default:
}

# Testify Assert
anil			assert nil assert.Nil(t, actual)
annil			assert not nil assert.NotNil(t, actual)
aeq				assert equal assert.Equal(t, expected, actual)
anerr			assert no error assert.NoError(t, err)

# Import
logrus			import logrus log "github.com/sirupsen/logrus"
*/
package main

import (
	"fmt"

	"strconv"

	"strings"

	alias "tutorial/alias.lib"
	"tutorial/lib"

	"rsc.io/quote"
)

var v rune

func init() {
	v = '1'
	fmt.Println("init 함수는 패키지가 로드될 때 호출된다.")
}

func main() {
	fmt.Println("========================== hello world ==========================")
	fmt.Println(quote.Hello())

	fmt.Println("========================== variables ==========================")
	var num = 1
	var str = "Hello, World!"
	num2 := 10
	var nums = []int{32, 64, 128}

	var (
		name   = "small-goliath"
		age    = 32
		weight = 60.3
	)

	fmt.Printf("num + num2 = %d\n", num+num2)
	fmt.Printf("print str: %s\n", str)
	fmt.Printf("my name is %s, age is %d and weight is %f.\n", name, age, weight)

	fmt.Println("========================== Constants and enum ==========================")
	// 상수와 열거형에 차이를 두지 않는다.
	const (
		RED = iota
		ORANGE
		YELLOW
	)
	fmt.Printf("RED: %d\n", RED)
	fmt.Printf("ORANGE: %d\n", ORANGE)
	fmt.Printf("YELLOW: %d\n", YELLOW)

	const (
		Run = 1 << iota
		Wait
		send
		receive
	)
	fmt.Printf("Run: %d\n", Run)
	fmt.Printf("Wait: %d\n", Wait)
	fmt.Printf("send: %d\n", send)
	fmt.Printf("receive: %d\n", receive)

	stat := Run | send
	if stat&Run == Run {
		fmt.Println("Run")
	}
	if stat&Wait == Wait {
		fmt.Println("Wait")
	}

	fmt.Println("========================== Control Statement ==========================")

	if age > 30 {
		fmt.Println("30대")
	} else if age < 30 {
		fmt.Println("10대 20대")
	} else {
		fmt.Println("30세")
	}

	if thirty := 30; age > thirty {
		fmt.Println("30대")
	} else if age < thirty {
		fmt.Println("10대 20대")
	} else {
		fmt.Println("30세")
	}

	switch age {
	case 30:
		fmt.Println("30세")
	case 10, 20:
		fmt.Println("10세 20세")
	default:
		fmt.Println("그 외")
	}

	switch thirty := 30; {
	case age > thirty:
		fmt.Println("30대")
	case age < thirty:
		fmt.Println("10대 20대")
	default:
		fmt.Println("30세")
	}

	i := 0
	switch i {
	case 0:
	case 1:
		Display("not fallthrough")
	}

	switch i {
	case 0:
		fallthrough
	case 1:
		Display("fallthrough")
	}

	fmt.Println("========================== loop ==========================")
	sum := 0
	for i := 0; i < 5; i++ {
		sum += i
	}
	fmt.Printf("sum: %d\n", sum)

	i = 11
	sum = 0
	for {
		i -= 1

		if i == 0 {
			break
		}

		if i%2 == 1 {
			sum += i
			continue
		}
		fmt.Printf("%d is even number. not continue!!!\n", i)
	}
	fmt.Printf("sum: %d\n", sum)

	i = 11
	sum = 0
LOOP:
	for {
		i -= 1

		if i%2 == 1 {
			sum += i
			break LOOP
		}
		fmt.Printf("%d is even number. not break LOOP!!!\n", i)
	}
	fmt.Printf("break LOOP!!! sum: %d\n", sum)

	for i, v := range nums {
		fmt.Printf("i: %d, v: %d\n", i, v)
	}

	for _, v := range nums {
		fmt.Printf("v: %d\n", v)
	}

	fmt.Println("========================== function ==========================")
	Display2("loop", 3, 2, 1)
	fmt.Println(DoubleAge(age))
	fmt.Println(DoubleAgeAndName(age, name))
	if v, err := ToInt("not number"); err != nil {
		fmt.Printf("정수가 아니야: [%s]\n", err)
	} else {
		fmt.Printf("%d는 정수야\n", v)
	}

	fmt.Printf("CallByValue 바꾸기 전 name: %s\n", name)
	SetCallByValue(name)
	fmt.Printf("CallByValue 바꾸기 후 name: %s\n", name)

	fmt.Printf("SetCallByReference 바꾸기 전 name: %s\n", name)
	SetCallByReference(&name)
	fmt.Printf("SetCallByReference 바꾸기 후 name: %s\n", name)

	fplus := func(x, y int) int {
		return x + y
	}
	fmt.Println(fplus(1, 1))

	fmt.Println(func(x, y int) int {
		return x + y
	}(1, 1))

	// closure
	addZip := ClosureName(".zip")
	addTar := ClosureName(".tar")
	fmt.Println(addZip("Clo"))
	fmt.Println(addTar("sure"))

	// defer
	WhatIsDefer()

	FuncArgs(3, Display3)

	fmt.Println(lib.IsDigit('d'))
	// fmt.Println(lib.isSpace(' '))
	fmt.Println(alias.IsDigit2('1'))
	fmt.Printf("init 함수가 호출 되었는지 확인: %c\n", v)

}

func FuncArgs(num int, f func(int, string)) {
	f(num, "나를 출력해줘")
}

func Display3(num int, str string) {
	fmt.Printf("num: %d, str: %s\n", num, str)
}

func ClosureName(suf string) func(string) string {
	return func(name string) string {
		if !strings.HasSuffix(name, suf) {
			return name + suf
		}
		return name
	}
}

func WhatIsDefer() {
	fmt.Println("WhatIsDefer() START!")
	defer Defer()
	fmt.Println("WhatIsDefer() END!")
}

func Defer() {
	fmt.Println("Defer END!")
}

func SetCallByValue(str string) {
	str = "바꿨지롱"
}

func SetCallByReference(str *string) {
	*str = "바꿨지롱"
}

func DoubleAge(age int) int {
	return age * 2
}

func DoubleAgeAndName(age int, name string) (int, string) {
	return age * 2, name + "!!!"
}

func ToInt(str string) (int, error) {
	return strconv.Atoi(str)
}

func Display(str string) {
	fmt.Printf("Display: %s\n", str)
}

func Display2(str string, num ...int) {
	Display(str)
	for i, v := range num {
		fmt.Printf("i: %d, v: %d\n", i, v)
	}
}

func Connecction() string {
	con := "Connection"
	return con
}

func SetConnecction(name string) {
}
