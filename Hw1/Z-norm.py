import math

Heightlist = [195,200,192,230,212,200,210,205,218,177,185,197]

WeightList = [96,98,86,140,116,92,117,113,136,81,79,92]

HeightMean = 201.74
WeightMean = 103.8333




StadordDivforH =0
StadordDivforW =0

def calcStadardDiv(list, mean):
    STDDiv =0
    for i in list:
       STDDiv += pow(i - mean,2)

    length = len(list)
    result = math.sqrt(STDDiv /(length-1))   
    return result


StadordDivforH = calcStadardDiv(Heightlist,HeightMean)
StadordDivforW = calcStadardDiv(WeightList,WeightMean)

def calcZScore(list, mean, StandordDiv):
    tempz = []
    
    for i in list:
        tempz.append((i - mean)/StandordDiv)
     

    return tempz

zForH = calcZScore(Heightlist,HeightMean,StadordDivforH)
zforW = calcZScore(WeightList,WeightMean,StadordDivforW)
def printzvals(list):
    for i in list:
        print(f"{i:.4f}", end="")


print(f"The New Z values for Heighs are")
printzvals(zForH)
print(f"The New Z values for Weights are ")
printzvals(zforW)

NewMeansFromzforH =0
NewMeansFromzforW =0

def calcMean(list):
    sumofmean =0
    for i in list:
        sumofmean += i
    
    tempsum = sumofmean/len(list)
    return tempsum
NewMeansFromzforH = calcMean(zForH)
NewMeansFromzforW = calcMean(zforW)


def Calcsamplevariance(list, mean):
    Samplevar =0
    for i in list:
       Samplevar += pow(i - mean,2)

    length = len(list)
    result = (Samplevar /(length-1))   
    return result



SVforH = Calcsamplevariance(zForH,NewMeansFromzforH)
SVforw = Calcsamplevariance(zforW,NewMeansFromzforW)

SDforH = calcStadardDiv(zForH,NewMeansFromzforH)
SDforw = calcStadardDiv(zforW,NewMeansFromzforW)

print(f"The Sample Variance for Height Is {SVforH}")
print(f"The Sample Variance for Height Is {SVforw}")

print(f"The Sample Standard Variance for Height Is {SDforH}")
print(f"The Sample Standard Variance for Height Is {SDforw}")