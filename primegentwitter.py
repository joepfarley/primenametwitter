#!/usr/bin/env python
import os
import sys
import tweepy
from time import sleep


CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def filterout(L1,L2):
    """ inplace substraction of two lists"""
    for i in L1:
        if i in L2:
            L2.remove(i)


def is_prime(n):
    """ check if n is prime"""
    i = 2
    if n <=1:
        return False
    Sqrt_Of_n = n**0.5
    while i <= Sqrt_Of_n:
        if n % i == 0:
            return False
        i += 1
    else:
        return True


def primeGen(number):
	while True:	
		if is_prime(number-1):
			yield(number-1)
		if is_prime(number+1):
			yield(number+1)
		if is_prime(number-1) and is_prime(number+1):
			api.update_status("%d and %d are twin prime numbers. #twinprime"% (number-1, number+1))
		if is_prime(number-1) or is_prime(number+1):sleep(900)
		number +=6
		



for i in primeGen(24):api.update_status("%d is a prime number. #isprime"% i)

#api.update_status("I'm not sure why, but I crashed. Here we go again in a minute. #primenumbers")
V
#sleep(60)

#for i in primeList:
	#api.update_status("%d is prime.#isprime"% i)
	#print("%d is prime. #isprime"% i) 
	#sleep(900)


