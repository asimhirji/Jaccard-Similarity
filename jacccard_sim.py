from natsort import natsorted
import glob

def main():
    filepath = glob.glob("/Users/asimhirji/Desktop/research/*.txt")
    #sorts files with a natural sort algorithm
    files = natsorted(filepath)

    

#iterates through all the files and matches files to compare
def file_iteration(f_list):
    directory_count = 0
    count = 0
    for i in range(len(f_list)):
        #skips every fourth file pair due to docgroup changes
        if (count == 3):
            count = 0
            continue
        
        prog_control(file_list[i],file_list[i+1])
        str1 = file_list[i]
        str2 = file_list[i+1]
        
        count += 1
        directory_count += 1

        #kills program when last file is reached
        if (directory_count = len(file_list) - 1):
            break


        
#needs to write out a new text file still
       
def prog_control(file1, file2):
    #reads both files and puts each sentence in a list
    file1 = open(file1, "r") 
    arr1 = file1.readlines()[3:]
    
    file2 = open(file2, "r")
    arr2 = file2.readlines()[3:]
  
    #filters sentences
    art1 = filter_list(arr1)
    art2 = filter_list(arr2)
    art1 = list(filter(None,art1))
    art2 = list(filter(None,art2))

    #find jaccard similarity between article
    value = jacc_compare(art1,art2)
        
#takes original sentence and filters anything not letter,space, or '     
def filter_list(f_list):
    for i in range(len(f_list))
        sentence = f_list[i]
        new_line = filter_str(sentence)
        f_list[i] = new_line
    return f_list

#works
#filters string to read only words
def filter_str(st):
    chars = st.split()
    new_str = ""
    for char in st:
        if (char.isalpha() or char == " " or char == "'"):
            new_str += char
    case_str = new_str.lower()
    return case_str

#compares sentences in different articles
def jacc_compare(list1,list2):
    nums_array = []
    for elem in list1:
        max_jacc = 0.0
        sent1 = elem

        for item in list2:
            sent2 = item
            jacc_coeff = jacc_calc(sent1,sent2)

            #checks for maximum jaccard value
            if (jacc_coeff > max_jacc):
                max_jacc = jacc_coeff
                
        nums_array.append(max_jacc)
    art_coeff = art_jacc(nums_array)
    return art_coeff

#works
#calculates jaccard similarity
def jacc_calc(str1,str2):
    a = set(str1.split())
    b = set(str2.split())
    c = a.intersection(b)

    return float(len(c)/(len(a) + len(b) - len(c)))

#works
#find average jaccard coeff for entire article
def art_jacc(arr):
    sum1 = 0.0
    for num in arr:
        sum1 += num
    avg = sum1 / len(arr)
    return avg

main()
