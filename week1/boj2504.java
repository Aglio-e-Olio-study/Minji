package week1;
import java.util.*;

public class boj2504 {
    public static void main(String[] args) {
        //입력
        Scanner sc=new Scanner(System.in);
        char[] string=sc.nextLine().toCharArray();
        
        // stack 생성
        Stack<Character> st=new Stack<>();
        int result=0;
        int tmp=1;
        sc.close();
        
        //반복문 돌면서 4가지 case에 대해 처리
        for (int i=0;i<string.length;i++){
            // 1. 여는 소괄호일 ㄸ
            if (string[i]=='('){
                tmp*=2;
                st.push(string[i]);
            }
            // 2. 여는 대괄호일 때
            else if (string[i]==')'){
                // 2-1. 스택이 비어있거나 마지막 문자가 여는 소괄호가 아닐 때
                if (st.isEmpty() || st.peek()!='('){
                    result=0;
                    break;
                }
                // 2-2. 직전 문자가 여는 소괄호일 때
                if (string[i-1]=='('){
                    result+=tmp;
                }
                // 2-3. 스택에서 여는 소괄호 제거&tmp 값 초기화
                st.pop();
                tmp/=2;
            }
            // 3. 여는 대괄호일 때
            else if (string[i]=='['){
                tmp*=3;
                st.push(string[i]);
            }
            // 4. 닫는 대괄호일 때
            else if (string[i]==']'){
                // 4-1. 스택이 비어있거나 마지막 문자가 여는 대괄호가 아닐 때
                if (st.isEmpty() || st.peek()!='['){
                    result=0;
                    break;
                }
                // 4-2. 직전 문자가 여는 대괄호일 때
                if (string[i-1]=='['){
                    result+=tmp;
                }
                // 4-3. 스택에서 여는 대괄호 제거&tmp 값 초기화
                st.pop();
                tmp/=3;
            }
        }
        // 5. 탐색 끝났는데 스택이 비어있지 않으면 올바르지 않은 경우
        if (!st.isEmpty()){
            result=0;
        }
        System.out.println(result);
    }
}
