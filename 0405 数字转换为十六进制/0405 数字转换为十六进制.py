#label: 位运算 difficulty: easy

class Solution:
    def toHex(self, num: int) -> str:
        #通过取余方法
        dict={10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
        hexRes=[]
        if num<0:
            num+=2**32#处理负数的方法
        if num==0:
            return '0'
        while num>0:
            figure=num%16
            num//=16
            if figure>=0 and figure<=9:
                hexRes.append(str(figure))
            else:
                hexRes.append(dict[figure])
        hexRes=hexRes[::-1]
        return ''.join(hexRes)#数组转换成字符
        
            


"""
首先拿到这题，比较简单的一个思路是把负数转换为正数的形式（因为我们知道，负数在计算机中的存放值=2^N+该负数，N为存储的位数）。

但是在JAVA中，这个思路会在num值为-1的情况下出现下标溢出的情况。这个问题还不知道原因。

于是我百度了一下，发现了一个更优秀的做法。也就是模拟电路加减的做法，把数字拿去和0xf相与，得到的结果就是数字的最后四位二进制代表的十进制数值。

然后继续把该数字算术右移四位，也就是相当于得到下一个四位二进制的值，以此类推。通过二进制的做法，规避了操作十进制数时负数的问题。

在这题里使用位运算需要注意不要超出八位数，因为负数的算术右移可以在正常右移结束后得到非零值，循环不会正确退出。

"""

class Solution {
    public String toHex(int num) {
        if (num == 0)
            return "0";
        char[] pat = { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f' };
        String ans = "";
        while (num != 0 && ans.length() <= 8) 
        {
            ans = pat[num & 0xf] + ans;
            num >>= 4;
        }
        return ans;

    }
}
