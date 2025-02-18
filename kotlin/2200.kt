/*
문제
다항식을 계산하기 위해 고안된 계산기가 있다. 이 계산기에는 0부터 9까지의 숫자와 +, x(곱하기), X, =의 14개의 키가 있다.
예를 들어 이 계산기를 이용하여 X^3 + X + 11을 계산하려면 X, x, X, x, X, +, X + 1, 1, = 을 누르면 된다.
또 X^3 + 2X^2 + 11을 계산하기 위해서는 X, +, 2, x, X, x, X, +, 1, 1, = 을 누르면 된다.
일반적인 계산기라면 X, +, 2, x, X, x, X, +, 1, 1, = 을 X + 2X^2 + 11로 인식하겠지만,
이 계산기는 추가 메모리가 없기 때문에 계산을 할 때에 계산 직전에 계산기에 저장되어 있던 값에 계산을 한다.
즉 X, +, 2, x, X, x, X, +, 1, 1, = 을 입력하면 계산기에는 차례로 X, X+2, X^2+2X, X^3+2X^2, X^3+2X^2+11 이 입력되는 것이다.
문제를 단순하게 하기 위해서 최고차항의 계수는 항상 1이라고 가정하자. 또 음수 계수는 고려하지 않기로 하자.
다항식이 주어졌을 때, 이 계산기로 주어진 다항식을 계산하려면 계산기를 최소 몇 번 눌러야 하는지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 다항식의 차수 N(1 ≤ N ≤ 10,000)이 주어진다.
다음 줄에는 다항식의 계수가 최고차항부터 주어진다. 최고차항의 계수는 항상 1이며 모든 계수는 0 이상이다. 모든 계수는 1,000,000,000을 넘지 않는다.

출력
첫째 줄에 계산기를 누르는 최소 횟수를 출력한다.


3
1 0 1 11

11
X
X x
X^2
X^2 x
X^3
X +
X + X
X + X +
X + X + 1
X + X + 11
X + X + 11 =

3
1 2 0 11

11
X
X +
X + 2
X + 2 x
X^2 + 2X
X^2 + 2X x
X^3 + 2X^2
X^3 + 2X^2 +
X^3 + 2X^2 + 1
X^3 + 2X^2 + 11
X^3 + 2X^2 + 11 =

3
1 0 0 11

9
X
X x
X^2
X^2 x
X^3
X^3 +
X^3 + 1
X^3 + 11
X^3 + 11 =

3
1 11 0 11

12
X
X +
X + 1
X + 11
X + 11 x
X^2 + 11X
X^2 + 11X x
X^3 + 11X^2
X^3 + 11X^2 +
X^3 + 11X^2 + 1
X^3 + 11X^2 + 11
X^3 + 11X^2 + 11 =

3
1 11 1 11

14
X
X +
X + 1
X + 11
X + 11 x
X^2 + 11X
X^2 + 11X x
X^3 + 11X^2
X^3 + 11X^2 +
X^3 + 11X^2 + X
X^3 + 11X^2 + X +
X^3 + 11X^2 + X + 1
X^3 + 11X^2 + X + 11
X^3 + 11X^2 + X + 11 =
 */
import java.io.BufferedReader
import java.io.InputStreamReader

 fun main(args: Array<String>) = with (BufferedReader(InputStreamReader(System.`in`))) {
    val n: Int = readLine()!!.toInt()
    val arr = readLine()!!.split(' ').map { it.toInt() }
    var count: Int = 1
    var zero_count: Int = 0

    for (v in arr) {
        if (v == 0) {
            zero_count++
        } else {
            if (v > 0 && v < 10) {
                count++
            } else {
                count += v.toString().length
            }
        }
    }

    count += ((2 * (n - 1)) + (n - zero_count))

    println(count)
 }