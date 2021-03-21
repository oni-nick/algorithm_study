package stack;

import java.util.Arrays;
import java.util.Stack;

class Solution {
    public int[] solution(int[] prices) {
        Stack<Integer> beginIdxs = new Stack<>();
        int i=0;
        int[] terms = new int[prices.length];

        beginIdxs.push(i);
        for (i=1; i<prices.length; i++) {
            while (!beginIdxs.empty() && prices[i] < prices[beginIdxs.peek()]) {
                int beginIdx = beginIdxs.pop();
                terms[beginIdx] = i - beginIdx;
            }
            beginIdxs.push(i);
        }
        while (!beginIdxs.empty()) {
            int beginIdx = beginIdxs.pop();
            terms[beginIdx] = i - beginIdx - 1;
        }

        return terms;
    }
    
    public static void main (String[] args) {
    	Solution temp = new Solution();
    	int[] tt = new int[] {1,2, 3, 2, 3, 1};
    	System.out.println(Arrays.toString(temp.solution(tt)));
    }
}
