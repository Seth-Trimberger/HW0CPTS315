import math

Heightlist = [195,200,192,230,212,200,210,205,218,177,185,197]

WeightList = [96,98,86,140,116,92,117,113,136,81,79,92]
#new range from 1,5


def minMaxfunc(list):
    Lmin = min(list)
    Lmax = max(list)

    newmin = 1
    newmax = 5

    NewVal =[]
    for i in list:
        NewVal.append(  (i-Lmin)/(Lmax-Lmin)* (newmax-newmin) + newmin )
    return NewVal

Hl = minMaxfunc(Heightlist)
WL = minMaxfunc(WeightList)

def printlist(list):

    for i in list:
        print(f"{i:.4f}", end=" ")

#printlist(Hl)
#printlist(WL)
def calcMean(list):
    sumofmean =0
    for i in list:
        sumofmean += i
    
    tempsum = sumofmean/len(list)
    return tempsum




def Calcsamplevariance(list, mean):
    Samplevar =0
    for i in list:
       Samplevar += pow(i - mean,2)

    length = len(list)
    result = (Samplevar /(length-1))   
    return result

def calcStadardDiv(list, mean):
    STDDiv =0
    for i in list:
       STDDiv += pow(i - mean,2)

    length = len(list)
    result = math.sqrt(STDDiv /(length-1))   

    return result


HlMean = calcMean(Hl)
WLMean = calcMean(WL)

HlSampVar = Calcsamplevariance(Hl,HlMean)
WLMSampVar = Calcsamplevariance(WL,WLMean)

HltdVar = calcStadardDiv(Hl,HlMean)
WLstdVar = calcStadardDiv(WL,WLMean)

print(f"{HlSampVar:.4f}")

print(f"{WLMSampVar:.4f}")

print(f"{HltdVar:.4f}")

print(f"{WLstdVar:.4f}")