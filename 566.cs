
public class Solution {
    public int[,] MatrixReshape(int[,] nums, int r, int c) {
        if (nums.Length != r * c) {
            return nums;
        }
        int i = 0; // row num
        int j = 0; // row index
        int[,] newNums = new int[r, c];
        foreach (int num in nums) {
            // System.Console.Write(num);
            if (j >= c) {
                j = 0;
                i++;
            }


            if (i >= r) {
                return nums;
            }


            newNums[i, j] = num;
            j++;
        }
        return newNums;
        // if (Array.Length(nums) != r * c) {
        //     return nums;
        // }
        // // int numsC = Array.Length(nums[0]);
        // // int numsR = Array.Length(nums) / numsC;

        // // int[,] newNums;
        // // for (int i = 0; i < r; i++) {
        // //     int[] row;
        // //     for (int j = 0; j < c; j++) {
        // //         row[] =
        // //     }
        // // }

    }
}