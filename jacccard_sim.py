from natsort import natsorted
import glob

def main():
    #must enter own filepath
    filepath = glob.glob()
    #sorts files with a natural sort algorithm
    files = natsorted(filepath)
    write_sim(files)

def write_sim(files):
    count = 0
    g_count = 0
    for i in range(len(files) - 1):
        
        if (count == 3):
            count = 0
            continue
    
        str1 = files[i]
        str2 = files[i+1]
        
        #gets document id number
        #need to change numbers in group_id1 and id1 depending on directory length
        group_id1 = str1[47:]
        id_count = 0
        for char in group_id1:
            if (char.isdigit()):
                id_count += 1
        id1 = str1[47: 46 + id_count]

        g_count = group_type(g_count,id1)
        control(str1,str2)
        count += 1
        
#prints group id for the document
def group_type(id_count, id_num):
    if (id_count == 0):
            print("docgroup" + id_num + "_G4vsG6: ", end = '')
            id_count += 1
    elif (id_count == 1):
            print("docgroup" + id_num + "_G6vsG8: ", end = '')
            id_count += 1
    elif (id_count == 2):
            print("docgroup" + id_num + "_G8vsG12: ", end = '')
            id_count = 0
    return id_count
        

def control(file1,file2):
    #reads both files and puts each sentence in a list
    f1 = open(file1, "r")
    f2 = open(file2, "r")

    #skips first 3 lines in each article.
    arr1 = f1.readlines()[3:]
    arr2 = f2.readlines()[3:]

    #filters sentences
    art1 = filter_list(arr1)
    art2 = filter_list(arr2)
    art1 = list(filter(None,art1))
    art2 = list(filter(None,art2))

    #find jaccard similarity between article
    value = jacc_compare(art1,art2)
    print(value)

#takes original sentence and filters anything not letter,space, or '     
def filter_list(f_list):
    for i in range(len(f_list)):
        sentence = f_list[i]
        new_line = filter_str(sentence)
        f_list[i] = new_line
    return f_list

#filters string to read only words
def filter_str(st):
    chars = st.split()
    new_str = ""
    for char in st:
        if (char.isalpha() or char == " " or char == "'"):
            new_str += char
    case_str = new_str.lower()
    return case_str

#compares sentences in dif ferent articles
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

#calculates jaccard similarity
def jacc_calc(str1,str2):
    a = set(str1.split())
    b = set(str2.split())
    c = a.intersection(b)

    return float(len(c)/(len(a) + len(b) - len(c)))

#find average jaccard coeff for entire article
def art_jacc(arr):
    sum1 = 0.0
    for num in arr:
        sum1 += num
    avg = sum1 / len(arr)
    return avg

main()
