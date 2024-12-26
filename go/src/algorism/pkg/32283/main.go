/*
문제
한별이는 길이 N의 이진수를 모두 모은 뒤 특별한 방식으로 정렬하여 사용하려 한다.
정렬 기준은 다음과 같다.

이진수 내의 1의 개수로 오름차순 정렬한다.
1의 개수가 같다면 이진수를 뒤집었을 때의 오름차순으로 정렬한다.
예를 들어, N이 3일 때 이진수는 다음 순서로 정렬된다.

000
100
010
001
110
101
011
111

어느날 친구 선린이가 찾아와 길이가 N인 이진수 하나를 주며 몇 번째 위치에 있는지 알려달라고 했다.
하지만 한별이는 다른 일이 많아 아직 이진수들을 정렬하지 못했다. 한별이를 도와주자!

입력
첫째 줄에 이진수의 길이 N이 주어진다.

둘째 줄에 길이N의 이진수 S가 주어진다.
이진수는 0으로 시작할 수 있다.

출력
주어진 이진수와 길이가 같은 모든 이진수를 정렬하였을 때, 주어진 이진수는 몇 번째 위치에 있는지 출력한다.

위치는
0번부터 시작한다.

제한
1 <= N <= 10

5
01101

22
*/
package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strings"
)

func main() {
	var reader *bufio.Reader = bufio.NewReader(os.Stdin)
	var writer *bufio.Writer = bufio.NewWriter(os.Stdout)

	defer writer.Flush()

	var n int
	var s string

	fmt.Fscanln(reader, &n)
	fmt.Fscanln(reader, &s)

	result := findBinaryPosition(n, s)
	fmt.Fprintln(writer, result)
}

func findBinaryPosition(n int, s string) int {
	binaryNumbers := make([]string, 1<<uint(n))
	for i := 0; i < len(binaryNumbers); i++ {
		binaryNumbers[i] = fmt.Sprintf("%0*b", n, i)
	}

	sortBinaryNumbers(&binaryNumbers)

	for index, binary := range binaryNumbers {
		if binary == s {
			return index
		}
	}

	return -1
}

func sortBinaryNumbers(binaryNumbers *[]string) {
	sort.Slice(*binaryNumbers, func(i, j int) bool {
		iCount := strings.Count((*binaryNumbers)[i], "1")
		jCount := strings.Count((*binaryNumbers)[j], "1")
		if iCount != jCount {
			return iCount < jCount
		}

		iReversed := reverseStr((*binaryNumbers)[i])
		jReversed := reverseStr((*binaryNumbers)[j])
		return iReversed < jReversed
	})
}

func reverseStr(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}
