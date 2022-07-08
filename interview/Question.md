# Memory address
heap: 該區域主要是用來儲存動態配置的變數
stack: 該區域主要儲存函數會使用到的所有資訊，包括區域變數等，而這裡會堆疊所有函數形成stack frame，每個stack frame之間會互相獨立，不會互相影響，遞迴函數也就是利用此特性。
static/global
code(text)

# Pointer
```clike=
int a: 這是一個整數型
int *a: 這是一個指標
int **a: 這是一個指向指標的指標，該指標指向一個整數型
int a[10]: 這是一個陣列，包含10個整數型
int *a[10]: 這是一個陣列，包含10個指標，該指標指向整數型。
int (*a)[10]: 這是一個指標，指向10個整數型的陣列。
int (*a)(int): 這是一個指標，指向一個函數，該函數有一個整數型的參數，並會回傳一個整數。
int (*a[10])(int): 這是一個陣列，包含10個指標，每個指標指向函數。

const int *foo: 這是一個指標，指向const int
int const *foo: 這是一個指標，指向const int
int* const foo: 這是一個const pointer，指向int
int const *const foo: 這是一個const pointer，指向const int
```
## void(*(*papf)[3])(char *);
typedef void(*pf)(char *);
pf(*papf)[3];
這是一個指標，指向一個陣列，陣列包含3個指標，裡面的每個指標都指向函數。

## How to write funtion pointer:
int add(int a, int b) {
    return a + b;
}
int main(void) {
    int (*op)(int a, int b);
    op = add;
    printf("%d\n", op(2, 5));
    return 0;
}

# Extern, static, Volatile & const volatile
extern: 在前面宣告extern，就代表這個變數在當前文件或先前的文件中有被定義過。
static: 在前面宣告static，就代表當函數結束後，會一直存在於記憶體中，變數不會消失。
volatile: 當宣告volatile，即代表該變數會被無預警的被修改，時常用於即時操作系統(RTOS)以及多執行緒的全域變數
const volatile: 當宣告這個時，表示該變數會被無預警的被修改，並且要表持唯讀不允許其他程式進行更改。

# Struct v.s. Union
struct: 表示每個成員都配置一段空間
union: 則是每個成員變數共用一段記憶體空間
union 占用的記憶體空間會以最大型態的為主。
struct 則會最佳化記憶體空間，有可能配置超過型態的大小。

# Define v.s. Inline
define: 文字替代
inline: 適用於簡單的函數宣告

# lvalue v.s. rvalue

# Array v.s. Pointer
Array配置的空間是連續的，pointer為不連續

# const int* p v.s. int* const q
前者是pointer且是const型態，代表p的值是唯讀的，不可更動
後者是const pointer，表示pointer不可更動

# Basic Question
int a[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
int *p = &(a + 1)[3];
printf("%d\n", *p);
Ans: 5

# ================
printf("size of BYTE = %d\n \
size of float = %d\n \
size of unsigned int = %d\n \
size of int = %d\n \
size of double = %d\n \
size of unsigned char = %d\n \
size of char = %d\n"
,sizeof(BYTE)          // 1
,sizeof(float)         // 4
,sizeof(unsigned int)  // 4
,sizeof(int)           // 4
,sizeof(double)        // 8
,sizeof(unsigned char) // 1
,sizeof(char));        // 1

# ================
int a[5]={1,2,3,4,5};
int *p=a;
*(p++)+=123;
*(++p)+=123;
Ans: a = {124, 2, 126, 4, 5}

# ================
int a[5] ={1,2,3,4,5};
int *p = (int *)(&a+1);
*(a+1) = ? // unexpected
(*p-1) = ? // 5

# ================
int x = 10, z = 3;
int *y;
*y = 5;
z = z + 1;
x = x + *y;
printf("x = %d\n", x);   // 15
printf("*y = %d\n", *y); // 5
printf("z = %d\n", z);   // 4

y = &x;                  
printf("y = %d\n", *y);  // 15

&z = y; // &z is lvalue, so this cannot access the value.
printf("z = %d\n", z);

# Question - Write a #define to print out ascii code of x.
#define FUN(x) (#X[0]) // define不需要;號，#會將X轉換為字串
printf("%d", FUN(a));  // %d就會將char轉成ascii code.

# Question - Write sum of 1+2+4+7+...+n.
最主要的就是 len = sizeof(arr) / sizeof(arr[0])

# Question - Write a macro to find maximum value of two value.
#define MAX(a, b) (a > b ? a : b) // 不需要加int

# Question - Declare a constant with preprocessor macro #define to indicate how many seconds are in a year.
#define SECONDS_PER_YEARS 60 * 60 * 24 * 365UL
// 重點在於要加上UL，表示unsigned long，佔 4 bytes
// 因為時間沒有負數且長度要大於2^16，因此要用4 bytes的型態去表示
//  8 bits (unsigned):           255
// 16 bits (unsigned):        65,535
// 32 bits (unsigned): 4,294,967,295
// 總時間為:              31,536,000

# Question - Write a MARCO to calculate the square of integer a.
#define square(x) (x * x)

# Question - Reverse string
把string分成一半，透過swap左右對調。

# Question - 寫出改⼤⼩寫跟判斷⼤⼩寫的函數
直接判斷字串'A' <= C，利用計數的方式，判斷大小寫數量。

# Question - 利⽤c語⾔，將字串＊str2接序在*str1後

# Question - Detect Capital

# Question - 不⽤strlen判斷字串長度

# Question - char比較
char b[]="123456";
char *a="123456";

# Question - 使⽤位元運算達成下列功能
N%4 
N/16
N*2

# Question - 交換兩數的值(不能使⽤變數幫忙)

# Question - ⽤⼀⾏程式判斷是否為2或3的冪次⽅

# Question - 請⽤bitwise實作出SWAP功能

# Question - 給兩個數 a b，判斷兩數是否互值

# Question - Write a code that check the input is a multiple of 3 or not without using division or mod

# Question - 給定⼀個正整數n，求出第n個質數

# Question - 給定⼀個正整數n，裡⾯有幾個質數

# Question - 寫⼀個link list的c程式(上機考)，link list的node內容為⼀個數字，有⼀個function會傳入⼀個integer，該function會將integer加入link list(要按照由⼩到⼤的順序)。

# Question - Write a function to find the middle field of singled-linked list without traverse whole list.

# Question - 判斷程式回傳值(指標)，判斷int溢位

# Question - Given two arrays, write a function to compute their intersection.

# Question - 保證 n ⼀定是上⾯五個數字之⼀ 不能⽤if 和 switch case , 請⽤你認為最快 的⽅法實作main
1. 
    extern void func1(void);
    extern void func2(void);
    extern void func3(void);
    extern void func4(void);
    extern void func5(void);
    void main(int n)
    {
        /*
        if n==1 execute func1;
        if n==2 execute func2;
        if n==3 execute func3;
        if n==4 execute func4;
        if n==5 execute func5;
        */
    }

2. 
    extern void func1(void);
    extern void func2(void);
    extern void func3(void);
    extern void func4(void);
    extern void func5(void);
    void main(int n)
    {
        /*
        if n==33 execute func1;
        if n==67 execute func2;
        if n==324 execute func3;
        if n==231 execute func4;
        if n==687 execute func5;
        */
    }

# Question
1. set the specific bit
2. clear the specific bit
3. inverse the specific bit (0->1; 1->0)
4. set 3 bit
5. clear 3 bit

# Question - Copy 4,5,6,7 bits of 0x1234567 to 0x145678f 1,2,3,4 bits

# Question - Write a code that check the input is a multiple of 3 or not without using division or mod

# Question - print 出100到-100 請寫兩種截然不同的寫法
# Question - 請寫⼀個會發⽣memory leak的程式
# Question - 請寫⼀個程式會發⽣pointer失效但是編譯是成功的
# Question - 寫⼀個 function 可傳入正整數參數 N，回傳 1 + 2 + 3 +...+N的和

# Question - Find the possible error
# Question - What is the possible error of below SQR function
# Question - SWAP函式 call by value 問你輸出值
# Question - SWAP函式 實作 call by reference
# Question - 指標頭腦運動操
# Question - 求出每次運算後A的值，實際題⽬可能跟我記得的不同，不過⼤致上類似
char A = 31;
1. A = A | 14;
2. A = A & (~)A;
3. A = A & ^A;


# ====== No answer ======
# Question - 實作找出第⼆⼤的陣列數值
# Question - 給 for loop, if, continue, break 問你輸出結果
# Question - 記憶體配置解釋: stack, heap, bss, data, text
# Question - 解釋static, volatile
# Question - 解釋Little-Endian, Big-Endian
# Question - 給⼀段Watchdog程式，問你有什麼問題和印出什麼結果