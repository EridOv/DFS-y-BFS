'''
Created on 27 abr. 2021

@author: erido
'''

from numpy.random.mtrand import randint
from random import randrange
from numpy import random, sqrt
from xmlrpc.client import boolean
from pickle import TRUE

class Arista2():
        A={}
        x={}
        y={}

def aristasMalla(lim,n, directo=boolean):
    for i in range(1,lim-n+1):
        a=i;a=str(a); 
        if (i%n!=0 & i<lim-n):
            b=i+1; b=str(b); 
            if directo==False: Arista2.A[a,b,]=[] 
            if directo==True: Arista2.A[a,b,'Directed']=[]
            b=i+n; b=str(b);
            if directo==False: Arista2.A[a,b,]=[]
            if directo==True: Arista2.A[a,b,'Directed']=[]
        if i%n==0:
            b=i+n; b=str(b);
            if directo==False: Arista2.A[a,b,]=[]
            if directo==True: Arista2.A[a,b,'Directed']=[]
            
    for i in range(lim-n+1,lim):
        a=i;a=str(a);
        b=i+1; b=str(b);
        if directo==False:Arista2.A[a,b,]=[]
        if directo==True: Arista2.A[a,b,'Directed']=[]
        
    return Arista2.A

def aristaErdosRenyi(n,m,dirigido=boolean):
    for i in range(1,m+1):
        b=randint(1,n+1); b=str(b)
        a=randint(1,n+1); a=str(a)
        if b!=a:
            if dirigido==False:Arista2.A[a,b,]=[] 
            if dirigido==True: Arista2.A[a,b,'Directed',]=[]            
        else:
            a=randint(n);a=str(a)
            if dirigido==False:Arista2.A[a,b,]=[] 
            if dirigido==True: Arista2.A[a,b,'Directed',]=[]          
    return Arista2.A
    
def aristasGilbert(n, p, dirigido=boolean):
    for i in range(1,n+1):
        a=randint(1,n+1)
        b=randint(1,n+1)
        volado=random.rand()
        while a==b: b=randint(1, n+1) 
        if a!=b:
            if (volado>p): 
                b=str(b);a=str(a)
                if dirigido==False:Arista2.A[a,b,]=[]
                if dirigido==True: Arista2.A[a,b,'Directed',]=[]  
    return Arista2.A

def aristasGeografico(n,r, dirigido=boolean):
    for i in range(1,n+1):
        Arista2.x[i]=randrange(1,10)
        Arista2.y[i]=randrange(1,10)
    
    for j in range(1,n):
        for k in range(1,n):
            d=sqrt((pow((Arista2.x[j]-Arista2.x[k]),2))+(pow((Arista2.y[j]-Arista2.y[k]),2)))           
            
            if d.real<r:
                if dirigido==False:Arista2.A[j,k,]=[]
                if dirigido==True:Arista2.A[j,k,'Directed',]=[]
    return Arista2.A
                
def aristaBarbasi(n,g,dirigido=boolean):
    orden=[]
    for i in range(1,n*g):
        a=randint(1,n+1)
        b=randint(1,n+1)       
        if a!=b:
            if (orden.count(a)<g):
                if orden.count(b)<g:
                    orden.append(a)
                    orden.append(b)
                    if dirigido==False:Arista2.A[a,b,]=[] 
                    if dirigido==True:Arista2.A[a,b,'Directed']=[] 
            else:
                i=i-1;
    return Arista2.A


def aristasDorogobsev(n, dirigido=boolean):
    orden=[]
    a=1; a=str(a);b=2;b=str(b)
    c=2; c=str(c);d=3;d=str(d)
    e=3; e=str(e);f=str(a)
    orden=[1,2,2,3,3,1]
    Arista2.A[a,b,]=[]
    Arista2.A[c,d,]=[]
    Arista2.A[e,f,]=[] 
    
    for i in range(4,n+1):
        long=(len(orden))-1
        ai=randrange(0,long,2)
        a=orden[ai]
        b=orden[(ai+1)]
        
        orden.append(i)
        orden.append(a)
        orden.append(i)
        orden.append(b)
        if dirigido==False:
            Arista2.A[i,a,]=[]
            Arista2.A[i,b,]=[]
        if dirigido==True:
            Arista2.A[i,a,'Directed',]=[]
            Arista2.A[i,b,'Directed',]=[]
        
    return Arista2.A