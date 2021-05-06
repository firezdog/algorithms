import java.util.*;

public class Solution {
    public int solution(int[] A)
    {
        Arrays.sort(A);
        if (A[A.length - 1] < 0) return 1;
        if (A.length == 1)
        {
            int singleton = A[0];
            if (singleton == 1) return 2;
            else return 1;
        }
        if (A[0] > 1) return 1;
        int next = 1;
        for (int i = 0; i < A.length - 1; i++) {
            if (A[i] <= 0) continue;
            if (A[i] == A[i + 1]) continue;
            if (A[i] != next) return next;
            next++;
        }
        if (A[A.length - 1] != next) return next;
        return A[A.length - 1] + 1;
    }
}
