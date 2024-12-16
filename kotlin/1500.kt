/*
문제
세준이는 정수 S와 K가 주어졌을 때, 합이 S인 K개의 양의 정수를 찾으려고 한다.
만약 여러개일 경우 그 곱을 가능한 최대로 하려고 한다.
가능한 최대의 곱을 출력한다.

만약 S=10, K=3이면, 3,3,4는 곱이 36으로 최대이다.

입력
첫째 줄에 두 수 S와 K가 주어진다.
K는 20보다 작거나 같고, S는 100보다 작거나 같으며 K보다 크거나 같다.

출력
첫째 줄에 정답을 출력한다.
답은 9223372036854775807보다 작다.


10 3

36


10 1

10


10 10

1


13 8

32


7 2

12
*/
import kotlin.math.pow

fun main() = with(System.`in`.bufferedReader()) {
    val (s, k) = readLine().split(" ").map { it.toLong() }
    var result = 1L

    if (s % k == 0L) {
        result = (s / k).toDouble().pow(k.toDouble()).toLong()
    } else {
        for(i in 0 until k - (s % k)) result *= s / k
        for(i in 0 until s % k) result *= s / k + 1
    }

    println(result)
}