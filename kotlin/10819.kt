

/*
문제
N개의 정수로 이루어진 배열 A가 주어진다.
이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.
|A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|

입력
첫째 줄에 N (3 ≤ N ≤ 8)이 주어진다.
둘째 줄에는 배열 A에 들어있는 정수가 주어진다.
배열에 들어있는 정수는 -100보다 크거나 같고, 100보다 작거나 같다.

출력
첫째 줄에 배열에 들어있는 수의 순서를 적절히 바꿔서 얻을 수 있는 식의 최댓값을 출력한다.


6
20 1 15 8 4 10

62
*/
import kotlin.math.max
import kotlin.math.abs

var answer = 0
fun solution(length : Int, result : IntArray, n : Int, arr : IntArray, visited : BooleanArray) {
    if (length == n) {
        var sum = 0
        for (i in 0 until n - 1) {
            sum += abs(result[i] - result[i + 1])
        }
        answer = max(answer, sum)
        return
    }

    loop@ for (i in 0 until n) {
        if (visited[i]) {
            continue@loop
        }

        result[length] = arr[i]
        visited[i] = true
        solution(length + 1, result, n, arr, visited)
        visited[i] = false
    }

}

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val a = readLine().split(' ').map { it.toInt() }.toIntArray()
    val visited = BooleanArray(n)

    solution(0, IntArray(n), n, a, visited)
    println(answer)
}