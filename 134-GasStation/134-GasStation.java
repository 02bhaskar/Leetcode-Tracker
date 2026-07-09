// Last updated: 7/9/2026, 3:08:13 PM
class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int totalGas = 0;
        int totalCost = 0;
        int currentFuel = 0;
        int startIndex = 0;

        for (int i = 0; i < gas.length; i++) {
            totalGas += gas[i];
            totalCost += cost[i];
            currentFuel += gas[i] - cost[i];

            if (currentFuel < 0) {
                startIndex = i + 1;
                currentFuel = 0;
            }
        }

        return totalGas >= totalCost ? startIndex : -1;
    }
}
