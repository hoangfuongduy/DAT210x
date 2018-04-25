
# coding: utf-8

# In[4]:


a = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']
b = 'abcdefghijklmnopqrstuvwxyz'
c = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


# In[5]:


def IsValidPassword(password):
    if len(password) < 8:
        print('Your password must contain at least 8 characters')
        password = input()
        IsValidPassword(password)
    if len(password) >= 8:
        inA = 0
        inB = 0
        inC = 0
        i = 0
        while i < len(password):
            if password[i] in a:
                inA += 1
            elif password[i] in b:
                inB += 1
            elif password[i] in c:
                inC += 1
            i = i + 1
        if inA == 0 or inB == 0 or inC == 0:
            print('Your password must contain at least 1 lowercase letter, 1 uppercase letter and 1 special character')
            password = input()
            IsValidPassword(password)
        else:
            print('Well done')          


# In[ ]:


yourpassword = input()
IsValidPassword(yourpassword)

