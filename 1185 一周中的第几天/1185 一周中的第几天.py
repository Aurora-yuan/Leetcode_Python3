#label: array difficulty: easy

"""
解题思路：

采用蔡勒公式
w=y+[y/4]+[c/4]-2c+[26(m+1）/10]+d-1
w：星期； w对7取模得：0-星期日，1-星期一，2-星期二，3-星期三，4-星期四，5-星期五，6-星期六
c：世纪（注：一般情况下，在公式中取值为已经过的世纪数，也就是年份除以一百的结果，而非正在进行的世纪，也就是现在常用的年份除以一百加一；不过如果年份是公元前的年份且非整百数的话，c应该等于所在世纪的编号，如公元前253年，是公元前3世纪，c就等于-3）
y：年（一般情况下是后两位数，如果是公元前的年份且非整百数，y应该等于cMOD100+100）
m：月（m大于等于3，小于等于14，即在蔡勒公式中，某年的1、2月要看作上一年的13、14月来计算，比如2003年1月1日要看作2002年的13月1日来计算）
d：日
[ ]代表取整，即只要整数部分。

"""

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        #w=y+[y/4]+[c/4]-2c+[26(m+1）/10]+d-1
        res=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
        
        if month==1 or month==2:
            month+=12
            year-=1
        c=year//100
        y=year%100
        w=y+y//4+c//4-2*c+26*(month+1)//10+day-1
        #print(c,y,month,day,w)
        return res[w%7] if w>0 else res[(w%7+7)%7]


