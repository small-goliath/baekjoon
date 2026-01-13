/*
N×M크기의 직사각형이 있다.
각 칸에는 한 자리 숫자가 적혀 있다.
이 직사각형에서 꼭짓점에 쓰여 있는 수가 모두 같은 가장 큰 정사각형을 찾는 프로그램을 작성하시오.
이때, 정사각형은 행 또는 열에 평행해야 한다.

[입력]
첫째 줄에 N과 M이 주어진다.
N과 M은 50보다 작거나 같은 자연수이다.
둘째 줄부터 N개의 줄에 수가 주어진다.

[출력]
첫째 줄에 정답 정사각형의 크기를 출력한다.

3 5
42101
22100
22101

9


2 2
12
34

1


2 4
1255
3455

4


1 10
1234567890

1


11 10
9785409507
2055103694
0861396761
3073207669
1233049493
2300248968
9769239548
7984130001
1670020095
8894239889
4053971072

49
 */

import kotlin.math.max
import kotlin.math.min

fun main() = with(System.`in`.bufferedReader()) {
    val (n, m) = readLine().split(" ").map { it.toInt() }
    val oblong = Array(n) { readLine().toCharArray() }
    var result = 0
    
    for (i in 0 until n) {
        for (j in 0 until m) {
            val maxRow = min(n-i, m-j)
            
            for (k in maxRow downTo 1) {
                if (oblong[i][j] == oblong[i][j + k - 1] &&
                    oblong[i][j] == oblong[i + k - 1][j] &&
                    oblong[i][j] == oblong[i + k - 1][j + k - 1]) {
                    result = max(k * k, result)
                }
            }
        }
    }

    println(result)
}