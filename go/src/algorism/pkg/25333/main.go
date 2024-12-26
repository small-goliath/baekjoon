/*
문제
Albert는 개구리 장난감을 이용한 놀이를 즐겨한다.
이 장난감은 우측으로 Acm 혹은 좌측으로 Bcm 점프할 수 있다.

예를 들어 현재 개구리 장난감의 위치가 0이고 A = 4, B = 2 라 하자.
아래 그림에서 음수는 처음 위치에서 좌측을, 양수는 우측을 나타내며 거리의 단위는 cm (centimeter) 이다.
( 그림 )
만약 개구리가 우측으로 점프를 한 번 한다면, 아래 그림처럼 4cm 만큼 이동한 위치에 착지하게 된다.
( 그림 )
이후 좌측으로 한 번 점프하면2cm 만큼 이동한 위치에 착지한다.
( 그림 )
여기서 다시 좌측으로 두 번 더 점프하면 총 4cm를 움직이게 되어 처음 위치에서 좌측으로 2cm 떨어진 지점에 착지한다.
( 그림 )

위 예제의 경우 개구리가 무한정 점프할 수 있더라도 처음 위치에서 1cm 떨어진 곳에 도달할 수 있는 방법은 없다.
이를 깨달은 Albert는 문득 궁금해졌다.
개구리가 무한정 점프할 수 있을 때, 처음 위치에서 우측으로 1cm, 2cm, ..., Xcm 떨어진 (총 X개의) 위치들 중 몇 곳에 도달할 수 있을까?
위 예제의 경우 A = 4, B = 2 라면 X = 10 일 때 처음 위치에서 우측으로 2cm, 4cm, 6cm, 8cm, 10cm 위치에 도달할 수 있으므로 정답은 5가 된다.

Albert를 도와 A, B, X가 주어졌을 때 답을 구해보자.

입력
입력 첫 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스는 한 줄에 세 개의 정수 A, B, X가 공백으로 구분되어 주어진다.

출력
각 테스트 케이스의 정답을 각 줄에 출력한다.

제한
1 ≤ T ≤ 20
1 ≤ A, B ≤ 1,000,000,000
1 ≤ X ≤ 2,000,000,000

7
4 2 10
2 4 11
5 3 15
20 22 2022
6 9 2000000000
1 1 2000000000
4 7 2

5
5
15
1011
666666666
2000000000
2

7
4 2 10
2 4 11
5 3 15
*/
package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var reader *bufio.Reader = bufio.NewReader(os.Stdin)
	var writer *bufio.Writer = bufio.NewWriter(os.Stdout)

	defer writer.Flush()

	var t int

	fmt.Fscanln(reader, &t)
	as := make([]int, t)
	bs := make([]int, t)
	xs := make([]int, t)

	var a, b, x int
	for i := 0; i < t; i++ {
		fmt.Fscanf(reader, "%d %d %d\n", &a, &b, &x)
		as[i] = a
		bs[i] = b
		xs[i] = x
	}

	for i := 0; i < t; i++ {
		gcd := gcd(as[i], bs[i])
		result := (xs[i]+gcd)/gcd - 1
		fmt.Fprintln(writer, result)
	}
}

func gcd(a, b int) int {
	for a > 0 {
		a, b = b%a, a
	}
	return b
}
