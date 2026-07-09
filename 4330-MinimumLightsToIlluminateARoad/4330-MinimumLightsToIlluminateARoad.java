// Last updated: 7/9/2026, 3:05:11 PM
import java.util.*;
class Solution {
    public int minLights(int[] lights) {
        int n = lights.length;
        int[] ravelunico = lights.clone();
        int[] diff = new int[n + 1];
        for (int i = 0; i < n; i++) {
            int v = lights[i];
            if (v > 0) {
                int l = Math.max(0, i - v);
                int r = Math.min(n - 1, i + v);
                diff[l]++;
                diff[r + 1]--;
            }
        }
        boolean[] visible = new boolean[n];
        int cur = 0;
        for (int i = 0; i < n; i++) {
            cur += diff[i];
            visible[i] = cur > 0;
        }
        int ans = 0;
        int i = 0;
        while (i < n) {
            if (visible[i]) {
                i++;
                continue;
            }
            ans++;
            int center = Math.min(i + 1, n - 1);
            int coverEnd = Math.min(n - 1, center + 1);
            i = coverEnd + 1;
        }
        return ans;
    }
}