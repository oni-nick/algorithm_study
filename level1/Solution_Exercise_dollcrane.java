package level1;
import java.util.Stack;

public class Solution_Exercise_dollcrane {
	public int pop_num(int[][] board, int[] moves) {	// 보드의 경우 현재 쌓여 있는 인형들의 상태들이 위쪽부터 나열되어 있음. 
		int pop_num=0;
		Stack<Integer> stack = new Stack<Integer>();
		for (int move : moves) {
			for(int j=0; j<board.length; j++) {			// 주어진 보드에서 위쪽부터 훑으면서 내려옴
				// "스택에 들어간다"라는 행동을 하는 경우는 0이 아닐때만 수행됨
				if(board[j][move - 1] != 0) {		// 인덱스는 0부터 시작하므로, move번째 열은 배열에서 move-1임 (선정한 열에서 가장 위쪽에 인형) 
					// 스택에 값이 들어가는 경우에, 스택이 비어있을 경우 추가적인 체크를 안해도 됨
					if(stack.isEmpty()) {
						stack.push(board[j][move - 1]);
						board[j][move - 1] = 0;
						break;
					}
					// 스택에 값이 있는 경우, 가장 바깥쪽 요소와 새로 들어가는 요소가 같은지 확인하는 절차 요구
					if(stack.peek() == board[j][move - 1]) {
						stack.pop();
						pop_num+=2;
					}
					else {
						stack.push(board[j][move - 1]);
					}
					board[j][move - 1] = 0;
					break;
				}
			}
		}
		return pop_num;
	}
}
