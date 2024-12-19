/*
문제
크기 N의 정수 배열 A가 있다.
다음 조건을 만족하도록 배열을 연속 구간으로 분할하는 것이 가능한지 판단하시오.

배열의 모든 원소가 정확히 하나의 구간에 포함된다.
각 구간의 크기는 1 이상 N 미만이며, 모든 구간의 크기는 같다.
각 구간에서 최솟값과 최댓값을 더한 값이 모든 구간에서 같다.

입력
첫째 줄에 배열의 크기 N이 주어진다. 
(2 <= N <= 100,000) 

둘째 줄에 A의 원소 A_{1}, A_{2}, A_{3}, ..., A_{N}이 공백으로 구분되어 주어진다. 
(1 <= A_{i} <= N) 

출력
조건을 만족하도록 배열을 분할하는 것이 가능하다면 1을, 그렇지 않다면 0을 첫째 줄에 출력한다.



9
1 9 4 3 5 7 6 8 2

1
[1,9,4], [3,5,7], [6,8,2]로 분할하면 각 구간에서 최솟값과 최댓값을 더한 값이 10으로 모두 같다.



3
1 1 1

1


4
1 3 2 4

0
*/
fun canDivideArray(n: Int, a: List<Int>): Int {
    for (k in 1 until n) {
        if (n % k != 0) {
            continue
        }
        val segments = a.chunked(k)
        val targetSum = segments[0].minOrNull()!! + segments[0].maxOrNull()!!

        if (segments.all { it.size == k && it.minOrNull()!! + it.maxOrNull()!! == targetSum }) {
            return 1
        }
    }
    return 0
}

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val a = readLine().split(' ').map { it.toInt() }.toList()

    println(canDivideArray(n, a))
}