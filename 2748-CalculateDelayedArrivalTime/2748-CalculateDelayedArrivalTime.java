// Last updated: 7/9/2026, 3:05:43 PM
class Solution {
    public int findDelayedArrivalTime(int arrivalTime, int delayedTime) {
        int time = arrivalTime + delayedTime;
        if (time>24){
            time=time%24;
        }
        if (time==24){
            return 0;
        }else{
            return time;
        }
    }
}