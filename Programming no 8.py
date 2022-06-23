#!/usr/bin/env python
# coding: utf-8

# Ans1)

# In[16]:


def addMatrices(a,b):
    print(f'Inputs:{a},{b}')
    if len(a) == len(b):
        out_matrix = []
        for ele in range(len(a)):
            if len(a[ele]) == len(b[ele]):
                out_matrix.append([])
                for sub_ele in range(len(a[ele])):
                    out_matrix[ele].append(a[ele][sub_ele]+b[ele][sub_ele])
            else:
                print('Both matrices must contains same no rows and columns')
                
        else:
             print('Both matrices must contains same no of rows and columns')
        print(f'Output:{out_matrix}')
            

addMatrices([[1,2,3],[4,5,6],[7,8,9]],[[9,8,7],[6,5,4],[3,2,1]])
addMatrices([[2,3,5],[1,1,1],[2,2,2]],[[4,3,5],[1,2,3],[3,2,1]])            
            
    


# Ans2)

# In[19]:


a = [[1,2,4], [4,5,6], [9,8,7]]
b = [[3,4,5], [6,7,8], [5,4,3]]

def multiply_matrice(a,b):
    output = []
    if len(a[0])  == len(b):
        for ele in range(len(a[0])):
            output.append([0 for ele in range (len(b[0]))])
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(b)):
                    output[i][j] +=a[i][k]*b[k][j]
        print(output)
    else:
        print('Matrix multiplication is not possible')
        
multiply_matrice(a,b)


# Ans3)

# In[20]:


a = [[1,2,3],[4,5,6],[7,8,9]]
b = [[1,2],[4,5],[7,8]]
c = [[1,2,3],[4,5,6]]

def generate_transpose(in_matrix):
    out_matrix = []
    for ele in range(len(in_matrix[0])):
        out_matrix.append([0 for i in range(len(in_matrix))])
    for i in range(len(in_matrix)):
        for j in range(len(in_matrix[i])):
            out_matrix[j][i] = in_matrix[i][j]
    print(f'{in_matrix} -> {out_matrix}')
        
generate_transpose(a)
generate_transpose(b)
generate_transpose(c)


# Ans4)

# In[22]:


def sortString():
    in_string = input("Enter a String: ").title()
    sorted_list = sorted(in_string.split(' '))
    print(' '.join(sorted_list))
    
sortString()


# Ans5)

# In[23]:


def removePunctuatuions():
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    in_string = input('Enter a String: ')
    out_string = ''
    for ele in in_string:
        if ele not in punctuations:
            out_string += ele
    print(out_string)
    
removePunctuatuions()

