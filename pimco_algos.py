#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 15:21:29 2022

@author: muertyn
"""
def calculate_savings_streak(total_days, complete_savings_streak):
    
    return complete_savings_streak/total_days

def calculate_incomplete_savings_streak(total_days, incomplete_savings_streak):
    
    return incomplete_savings_streak/total_days

def calculate_login_streak_ratio(total_days, login_streak):
    
    return login_streak/total_days

def calculate_money_deposited(total_days, money_deposited_streak):
    
    return money_deposited_streak/total_days

def calculate_financial_goal_ratio(total_days, financial_goal_streak):
    
    return  financial_goal_streak/total_days


def calculate_score(total_days, complete_savings_streak, incomplete_savings_streak, login_streak, money_deposited_streak, financial_goal):
    """
    We calculate a person's score (out of 100) by using a weighted average that is dependent on the following factors:
    
        Savings streak ratio: sum of days where this person deposited the entire target amount over duration (in days) of their goal 
        Incomplete savings streak ratio: sum of days where this person deposited the entire target amount over duration (in days) of their goal
        Login streak: sum of days where this person logged in at least once over the duration (in days) of their goal
        Money deposited ratio: sum of the days where this person contributed to their goal but not the full amount of the goal over duration (in days) of their goal
        Financial goal ratio: sum of the days where the goal was met in its entirety OR more over duration (in days) of their goal
        

    """
    
    complete_savings_streak_ratio = calculate_savings_streak(total_days, complete_savings_streak)
    
    incomplete_savings_streak_ratio = calculate_incomplete_savings_streak(total_days, incomplete_savings_streak)
    
    login_streak_ratio = calculate_login_streak_ratio(total_days, login_streak)
    
    money_deposited_ratio = calculate_money_deposited(total_days, money_deposited_streak)
    
    financial_goal_ratio = calculate_financial_goal_ratio(total_days, financial_goal)
    
    return (.25*complete_savings_streak_ratio+ .10*incomplete_savings_streak_ratio + .35*login_streak_ratio + .20*financial_goal_ratio + .10*money_deposited_ratio)*100





def recommendations(emergency_fund, retirement, trad_ira, roth_ira, stock_prof, savings):
    recommendation = "Your other accounts are looking good! Your stock portfolio awaits for more money to work with!"
    stock_minus_savings = stock_prof - savings
    
    if emergency_fund < 1000:
        recommendation = "It looks like your emergency fund isn't up to snuff. Let's contribute to that today!"
    
    elif emergency_fund > retirement:
        if roth_ira < trad_ira:
            recommendation = '"Time in the market beats timing the market". How about increasing your capital within your Roth IRA?'
        else:
            recommendation = "Take advantage of all the tax benefits from your 401k. Let's put your money to work."
    
    elif stock_minus_savings > stock_prof*.2:
        recommendation = "Let's make sure that you have more liquid assets. Invest into your savings account."
        
    return recommendation




















