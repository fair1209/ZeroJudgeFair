#a3
M ,D=map(int ,input().split())
S=(M*2+D)%3
print("普通" if S==0 else ("吉" if S==1 else "大吉"))
##------多重條件的短寫（巢狀 / 替代 if-elif-else）^^