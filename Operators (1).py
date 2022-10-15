#!/usr/bin/env python
# coding: utf-8

# ### Operators

#  #### Arthematic
#  #### Relational
#  #### logical
#  #### Assignment
#  #### Bitwise operators
#  #### Identify operators
#  #### Membership operators

# ### * Arthematic operators

# #### 1.Addition(+)

# In[20]:


x=10
y=20


# In[21]:


x+y


# #### 2.subtraction(-)

# In[22]:


x-y


# #### 3.multiplication(*)

# In[23]:


x*y


# #### 4.division(/)(

# In[24]:


x/y


# In[25]:


y/x


# #### 5.modulus(%)(returns remainder)

# In[26]:


x%y


# #### if x<y returns x

# In[27]:


y%x


# #### if x>y returns remainder

# #### 6.exponent(**)

# In[28]:


x**y


# #### 7.floordivision(//)(returns quotient)

# In[29]:


x//y


# #### if x<y returns 0

# In[30]:


y//x


# #### if x>y returns returns quotient

# ### *Relational operators
# #### used for conditional statements

# #### 1.Equal to(==)

# In[34]:


a=5
b=3
a==b


# #### 2.Not equal to(!=)

# In[35]:


a!=b


# #### 3.Greaterthan(>)

# In[43]:


a>b


# #### 4.lessthan(<)

# In[44]:


a<b


# #### 5.Greaterthan or equal to(>=)

# In[45]:


a>=b


# #### 5.lessthan or equal to(<=)

# In[46]:


a<=b


# ### *Logical operators

# #### 1.AND(&)
# #### returns true if both conditions are satisfied.

# In[55]:


x=5
y=9
z=3
(x>y) and (y>z)


# In[52]:


(x<y)&(y>z)


# #### 2.OR(|)

# In[57]:


(x>y) or (y>z)


# In[59]:


(x<y)|(y>z)


# In[105]:


x>10 or y>1


# ### 3.NOT

# In[5]:


x=False
print(~ x)


# In[7]:


not(x>y and y<z)


# ### *Assignment Operators

# #### assigns value to leftside operand

# #### += , -= , /= , *= , %= , **= , //=  , &= , ^= , \= , >>= , <<=

# In[71]:


p=11
q=8
p+=q
p


# In[113]:


a=5
b=3
a-=b
a


# In[114]:


a*=b
a


# In[115]:


a/=b
a


# In[116]:


a**=b
a


# In[117]:


a//=b
a


# In[118]:


a%=b
a


# In[107]:


a=5
b=3
a^=b
a


# In[108]:


a|=b
a


# In[109]:


a>>=b
a


# In[111]:


a=5
b=3
a<<=b
a


# In[112]:


a=5
b=3
a&=b
a


# ### Escape Character
# #### To insert characters that are invalid in a String we can use escape character.
# #### An escape character starts with a blackslash ' \ ' then character you want to insert.

# In[140]:


v='vamsi's Home'
v


# In[141]:


v="vamsi"s Home"
v


# In[138]:


v='vamsi\'s Home'
v


# In[139]:


v="vamsi\"s Home"
v


# ### *Bitwise operators
# ####(used to compare binary numbers)

# #### 1.AND(&)

# In[34]:


x=5
y=3
z=2
(x<y)&(y>z)


# #### 2.OR(|)

# In[35]:


(x<y|y>z)


# #### 3.XOR(^)

# In[36]:


(x<y)^(y>z)


# #### 4.NOT(~)

# In[37]:


~(x<y)


# #### 5.leftshift(<<)

# In[38]:


x<<y


# #### 6.rightshift(>>)

# In[23]:


x>>z


# ### *Identify operators
# #### is , is not

# #### 1.is - returns true if the both variables are the same object.

# #### 2.is not - returns true if both the variables are not same object.

# ### *Membership operators

# #### 1.in - returns true if a sequence with the specified value is present in the object.

# #### 2.not in - returns true if a sequence with the specified value is not present in the object
