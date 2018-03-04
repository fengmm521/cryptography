#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding: utf-8
#客户端调用，用于查看API返回结果

# from magetool import urltool

import sys
import os
import time
import binascii

#http://blog.csdn.net/crylearner/article/details/38521685

def R(Data,r):
    x = Data>>r
    return x

def listRR(lst, k): #k>0左移，k<0右移
    return lst[k:] + lst[:k]


def strToHex(pstr):
    e = 0   #暂存结果
    for i in pstr:
        d = ord(i)  #单个字符转换成ASCii码
        e = e*256 + d   #将单个字符转换成的ASCii码相连
    return e

def hexToStr(hexstr):
    c = binascii.a2b_hex(hexstr) #转换成ASCii编码的字符串
    return c

def main():
    d = 0x100
    t = int(d)
    print t,type(t)
    o = oct(d)
    print o,type(o)    #8进制字符串
    h = hex(d)
    print h,type(h)
    b = bin(d)      #2进制字符串
    print b,type(b)

    s = 'a'
    x = ord(s)
    print x,type(x),bin(x),chr(97)

    stmp = chr(x)     #整数传字符

    i = int(b,2)
    print i,type(i)

    r = R(d, 2)
    print r,type(r)




    s = 'abc'
    bs = bytes(s)
    print bs,type(bs)
    bsa = bytearray(s)
    print bsa,type(bsa),len(bsa),bsa[0],R(bsa[1], 1)

def binstrToHexStr(binstr):
    ostr = ''
    l = len(binstr)
    c = l/8
    print l,c
    for n in range(c):
        k = n*8
        tmpbin = '0b' + binstr[k:k+8]
        print n,k,tmpbin,hex(int(tmpbin,2))
        intdat = int(tmpbin,2)
        hexstr = hex(intdat)[2:]
        if len(hexstr) < 2:
            hexstr = '0' + hexstr
        ostr += hexstr
    return ostr

des_iptable = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,  
    62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,  
    57, 49, 41, 33, 25, 17,  9, 1, 59, 51, 43, 35, 27, 19, 11, 3,  
    61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]

des_keyselecttable = [57,49,41,33,25,17,9,1,58,50,42,34,26,18,
                      10,2,59,51,43,35,27,19,11,3,60,52,44,36,
                      63,55,47,39,31,23,15,7,62,54,46,38,30,22,
                      14,6,61,53,45,37,29,21,13,5,28,20,12,4]

def DESIP(datlist):
    print len(des_iptable),len(datlist)
    outlist = ''
    for i in range(64):
        outlist += datlist[des_iptable[i]-1]
    return outlist

def conventKey(keylist):
    kstr = ''
    for n in range(len(keylist)):
        if (n + 1) % 8 == 0:
            continue
        kstr += keylist[n]
    return kstr

def DESKeySelect(keylist):
    ostr = ''
    for i in range(len(keylist)):
        ostr += keylist[des_keyselecttable[i]-1]
    return ostr

def conventStrToBinList(instr):
    bostr = ''

    l = len(instr)
    c = l/2

    for n in range(c):
        k = n*2
        d = '0x' + instr[k:k+2]

        t = int(d,16)
        bstr = bin(t)
        tmpstr = bstr[2:]
        hexstr = hex(int(bstr,2))[2:]
        if len(hexstr) < 2:
            hexstr = '0x0' + hexstr
        else:
            hexstr = '0x' + hexstr
        
        tstr = tmpstr
        if len(tmpstr) < 8:
            offset = 8 - len(tmpstr)
            tstr = (offset*'0' + tmpstr)
        print d,t,bstr,hexstr,tstr
        bostr += tstr

    print bostr,'1'
    return bostr

def DESIPLR(instr = '02468aceeca86420'):
    bstrs = conventStrToBinList(instr)
    pstr1 = DESIP(bstrs)
    print pstr1
    hexstr = binstrToHexStr(pstr1)
    print hexstr

def des(intstr = '02468aceeca86420',keystr = '0f1571c947d9e859',outstr = 'da02ce3a89ecac3b'):

    bostr = ''

    l = len(keystr)
    c = l/2

    for n in range(c):
        k = n*2
        d = '0x' + keystr[k:k+2]

        t = int(d,16)
        bstr = bin(t)
        tmpstr = bstr[2:]
        hexstr = hex(int(bstr,2))[2:]
        if len(hexstr) < 2:
            hexstr = '0x0' + hexstr
        else:
            hexstr = '0x' + hexstr
        
        tstr = tmpstr
        if len(tmpstr) < 8:
            offset = 8 - len(tmpstr)
            tstr = (offset*'0' + tmpstr)
        print d,t,bstr,hexstr,tstr
        bostr += tstr

    print bostr,'1'

    ks1 = conventKey(bostr)
    ks2 = DESKeySelect(ks1)
    print ks2
    

    # bostr2 = DESIP(bostr)
    # print bostr2,'2'
    # bstrr = listRR(bostr2, 1)
    # print bstrr

    # ostr = binstrToHexStr(bstrr)
    # print ostr

    # bd = '0b1100001' #a
    # print chr(int(bd,2))


def test():
    # x = 0*'0'
    # print x
    DESIPLR()

if __name__ == '__main__':
    # main()
    # des()
    test()

