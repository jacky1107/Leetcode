#include <stdlib.h>
#include <stdio.h>

int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    printf("%d\n", numsSize);

    *returnSize=2;
    int *arr=(int *)malloc((*returnSize)*sizeof(int));
    for(int i=0;i<numsSize;i++){
        for(int j=i+1;j<numsSize;j++){
            if(nums[i]+nums[j]==target){
                arr[0]=i;
                arr[1]=j;
                break;
            }
        }
    }

    return arr;
}

int main() {
    int nums[] = {2, 7, 11, 15};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int target = 9;
    int *returnSize;
    int *res = twoSum(nums, numsSize, target, returnSize);
    return 0;
}