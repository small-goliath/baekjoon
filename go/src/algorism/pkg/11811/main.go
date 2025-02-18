/*
문제
젊은 제다이 이반의 임무는 데스스타에 침투하여 파괴하는 일이다.
데스스타를 파괴하기 위해서는 길이 N의 음이 아닌 정수 수열 ai가 필요하다.
그러나 이반은 이 수열을 가지고 있지 않다.
대신 그에게는 오랜 친구 다스 베이더에게 받은 쪽지가 하나 있다.
이 쪽지에는 그 수열이 만족해야 하는 조건이 적혀 있다.

이 쪽지에는 크기 N의 정사각 행렬이 있는데, i번째 행 j번째 열에 적힌 숫자는 ai와 aj에 비트연산 and를 수행한 결과값이다.
하지만 안타깝게도 광선검에 의해 쪽지가 손상되었고 이반은 행렬의 주 대각선에 있는 숫자를 읽을 수 없게 되었다.
원래 배열을 재구성하여 임무를 수행해야 하는 이반을 도와주자.

답은 유일하지 않을 수 있지만, 항상 존재하도록 주어진다.

입력
입력의 첫 번째 줄에는 행렬의 크기 N (1 ≤ N ≤ 1 000)이 주어진다.
다음 N개의 줄에는 행렬의 각 원소인 N개의 숫자 mij (1 ≤ mij ≤ 109)가 주어진다.

출력
정확히 한 줄에 문제의 조건을 만족하는 N개의 음이 아닌 정수를 출력한다.
각 정수는 109보다 같거나 작아야 한다. 답이 여러 개인 경우 아무거나 출력한다.

3
0 1 1
1 0 1
1 1 0

1 1 1

5
0 0 1 1 1
0 0 2 0 2
1 2 0 1 3
1 0 1 0 1
1 2 3 1 0

1 2 3 1 11
*/
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	var reader *bufio.Reader = bufio.NewReader(os.Stdin)
	var writer *bufio.Writer = bufio.NewWriter(os.Stdout)

	defer writer.Flush()

	line, _ := reader.ReadString('\n')
	n, _ := strconv.Atoi(strings.TrimSpace(line))

	hint := make([][]int, n)
	for i := 0; i < n; i++ {
		hint[i] = make([]int, n)
	}

	for i := 0; i < n; i++ {
		line, _ := reader.ReadString('\n')
		strArr := strings.Fields(line)

		arr := make([]int, n)
		for i, str := range strArr {
			arr[i], _ = strconv.Atoi(str)
		}
		hint[i] = arr
	}

	result := make([]int, n)

	for i := 0; i < n; i++ {
		result[i] = hint[i][0]
		for j := 1; j < n; j++ {
			result[i] |= hint[i][j]
		}
	}

	for i := 0; i < n; i++ {
		fmt.Fprintf(writer, "%d ", result[i])
	}
}
