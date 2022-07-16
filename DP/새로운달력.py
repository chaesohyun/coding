if __name__ == '__main__':
    T=int(input())

    Case=[]
    for i in range(T):
        Case.append(list(map(int, input().split())))

    line_res=[]
    for x in Case:
        M=x[0]
        DM=x[1]
        DW=x[2]
        line=0
        for i in range(M):
            if i==0:
                if DM%DW==0:
                    line=DM//DW
                    line=line*M
                    break
                else:
                    line=DM//DW +1
                    na=DM%DW
            else:
                line=line+1
                x=(DM-(DW-na))%DW
                if x==0:
                    line=line+((DM-(DW-na))//DW)
                else:
                    line=line+(DM-(DW-na))//DW +1
        line_res.append(line)

    for i in range(T):
        x=i+1
        y=line_res[i]
        print("Case #%d: %d" %(x, y))



