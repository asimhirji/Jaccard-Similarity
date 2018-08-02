from natsort import realsorted, ns
import glob
import operator

def main():
    minimum = 1.0
    a = []
    #enter file location
    file = open(, "r")
    for line in file:
        str1 = line.split('\n')
        str1 = list(str1)

        #getting rid of empty elements after split
        for i in range(len(str1)):
            if not (str1[i] == ''):
                a.append(str1[i])
    sorter(a)

#sorts jaccard similarity values               
def sorter(a):
    val_dict = {}
    for item in a:
        str2 = item.split(' ')
        str2 = list(str2)

        str2[1] = float(str2[1])
        val = str2[1]
        str3 = str(str2[0])
        val_dict[str3] = val


    list1 = sorted(val_dict.items(), key=operator.itemgetter(1))
    
    #print simmilarities in order from least to greatest
    for item in list1:
        line = str(item)
        st =""
        for char in line:
            if (char.isalnum() or (char == ':') or (char == " ") or (char == ".")):
                st += char

        print(st)
                
   
main()
