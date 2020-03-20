import java.util.*;

public class SmallestInt {
    public int SmallestInt(int[] A)
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
        for (int i = 1; i < A.length; i++) {
            if (A[i] <= 0) continue;
            if (A[i - 1] == A[i]) continue;
            if (A[i] != A[i - 1] + 1) return A[i - 1] + 1;
        }
        return A[A.length - 1] + 1;
    }
}
