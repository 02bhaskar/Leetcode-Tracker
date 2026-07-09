// Last updated: 7/9/2026, 3:05:35 PM
class Solution {
    public int sumOfTheDigitsOfHarshadNumber(int x) {
        int sum = 0, temp = x;
        while (temp > 0) {
            sum += temp % 10;
            temp /= 10;
        }
        return x % sum == 0 ? sum : -1;
    }
}
