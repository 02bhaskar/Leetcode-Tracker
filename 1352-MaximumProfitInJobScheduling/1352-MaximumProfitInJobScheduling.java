// Last updated: 7/9/2026, 3:05:57 PM
import java.util.*;

class Solution {
    private int[][] jobs;
    private int[] dp;

    public int jobScheduling(int[] startTime, int[] endTime, int[] profit) {
        int n = startTime.length;

        jobs = new int[n][3];
        for (int i = 0; i < n; i++) {
            jobs[i][0] = startTime[i];
            jobs[i][1] = endTime[i];
            jobs[i][2] = profit[i];
        }

        Arrays.sort(jobs, (a, b) -> Integer.compare(a[0], b[0]));

        dp = new int[n];
        Arrays.fill(dp, -1);

        return dfs(0);
    }

    private int dfs(int i) {
        if (i >= jobs.length) {
            return 0;
        }

        if (dp[i] != -1) {
            return dp[i];
        }

        int next = findNext(jobs[i][1]);

        int take = jobs[i][2] + dfs(next);
        int skip = dfs(i + 1);

        return dp[i] = Math.max(take, skip);
    }

    private int findNext(int endTime) {
        int left = 0, right = jobs.length;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (jobs[mid][0] < endTime) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return left;
    }
}