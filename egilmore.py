#!/usr/bin/env python

import tweepy
import random
import datetime

class TwitterAPI:

    def __init__(self):
        '''connect to twitter account; private information removed'''

        consumer_key = "XXXXXXXXXX"
        consumer_secret = "XXXXXXXXXX"
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = "XXXXXXXXXX"
        access_token_secret = "XXXXXXXXXX"
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message):
        '''post tweet'''

        self.api.update_status(status=message)


def get_first():
    '''generate first name'''

    part1 = ["Sweet", "Bunn", "Pen", "Mar", "Lill", "Soph", "Whit", "Marc",
            "Lyd", "Camm", "Oph", "Clem", "Luc", "Ell", "Conc", "Esmer", 
            "Glor", "Ad", "Adell", "Clar", "Els", "Mill", "Mir", "Viv", 
            "Mam", "Cel", "Myrtl", "Kitt", "Hatt", "Fann", "Gold", "Del", 
            "Bess", "Net", "Bitt", "Bab", "Siss", "Lac", "Bonn"]
    part2 = ["e", "ie", "y", "ilyn", "ella", "iney", "ine", "ia", "elda", 
            "ilda", "icent" "ivia", "illa", "entine", "ie", "ie", "ie", 
            "ie", "ie", "y", "y", "ilyn", "ian", "ine", "ia", "ie", "ie", 
            "ie", "ie", "ie", "ie", "ie", "ie", "y", "y", "ielle", "ie", 
            "ie", "ie", "ie", "ie", "ie", "y", "y", "y", "ey", "ey", "ey", 
            "ey", "ey", "ey", "ey", "ey", "ey", "ee", "e"]
    return str(random.choice(part1) + random.choice(part2))

def get_middle():
    '''small chance of middle initial "Q"'''

    part1 = [" Q", "", "", "", "", "", "", "","", "", "", "", "", "", "", 
            "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 
            "", "", "", "", "", "", "", "", "", "", "", ""]
    return str(random.choice(part1))

def get_last():
    '''generate last name'''

    part1 = ["Nel", "Charles", "Bill", "Whit", "McLear", "Hil", "Con", 
            "Ruther", "Bran", "King", "Arl", "Town", "Bell", "Fitz", 
            "Port", "Daven", "Chap", "Coop", "Cas", "Don", "Fin", "Lang", 
            "Lind", "Merr", "Pres", "Wes", "Hes", "Win", "New", "Welles", 
            "Fink", "Roths", "Lock", "Rich", "Els", "Worth", "Ald", "Ash", 
            "Pier"]
    part2 = ["son", "ton", "ing", "ington", "ingsworth", "rad", "ford", 
            "port", "thorne", "child", "amy", "wood", "igan", "send", 
            "ley", "taker", "mont", "stead", "mont", "tor", "cey", "tey", 
            "nett", "man", "ner", "ter", "wright", "mond", "alden", 
            "alton", "verly", "sly", "kin", "erton", "kins", "strop", 
            "ingly", "scott", "send", "sworth", "ridge", "well", "pont"]
    return str(random.choice(part1) + random.choice(part2))

def get_sport():
    '''generate sporting event'''

    part1 = ["Enjoying", "Enduring", "Dressing for", "Watching", "At", 
            "Attending", "Arriving to", "Leaving", "Suffering through", 
            "Home from", "Going to", "Heading to"]
    part2 = ["this", "this", "this", "this", "this", "that", "that", 
            "that", "Richard's", "Rory's", "some", "some", "the", "the", 
            "the", "the", "the", "the", "the", "the", "the", "the"]
    part3 = ["ridiculous", "first-class", "charitable", "fundraising",
            "European", "infuriating", "black tie", "atrocious", 
            "prestigious", "country club", "elite", "sophisticated", 
            "unsophisticated", "charity","alumni"]
    part4 = ["golfing", "tennis", "dressage", "yachting", "Harvard-Yale", 
            "croquet", "sailing", "polo", "Equestrian"]
    part5 = ["championship", "cup", "game", "Grand Prix", "invitational", 
            "tournament", "match", "final", "regatta"]
    string = random.choice(part1) + " " + random.choice(part2) + " "
    if (random.choice([True, True, False])):
            string += random.choice(part3) + " "
    string += random.choice(part4) + " " + random.choice(part5)
    return string

def get_party():
    '''generate social/party event'''

    part1 = ["Enjoying", "Furious about", "Enduring", "Criticizing", 
            "Planning", "Dressing for", "Shopping for", "Fixing", "At", 
            "Attending", "Arriving to", "Leaving", "Suffering through", 
            "Home from", "Going to", "Heading to", "Finalizing", 
            "Paying for", "Paying caterers for", "Arranging", "Preparing", 
            "Organizing", "Picking flower arrangements for", 
            "Hiring waitstaff for"]
    part2 = ["my", "my", "my", "my", "my", "my", "this", "this", "this", 
            "this", "this", "this", "that", "that", "that", "Richard's", 
            "Rory's", "Lorelei's", "some", "some", "the", "the", "the", 
            "the", "the", "the"]
    part3 = ["ridiculous", "absurd", "untenable", "imbecilic", 
            "transatlantic", "first-class", "charity", "charitable", 
            "fundraising", "infuriating", "black tie", "atrocious", 
            "presitigious", "country club", "aristocratic", "elite", 
            "highbrow", "sophisticated", "unsophisticated", "horse-drawn"]
    part4 = ["DAR", "rare books", "business", "cocktail", "debutante", 
            "tea", "alumni", "Yale", "birthday", "coming out", 
            "retirement", "holiday", "anniversary", "graduation", 
            "ladies'", "wedding"]
    part5 = ["party", "party", "gala", "gala", "ball", "ball", "soiree", 
            "dinner", "luncheon", "luncheon", "symposium", "trip", 
            "cotillion", "reunion", "reception","reception", "ceremony"]
    string = random.choice(part1) + " " + random.choice(part2) + " " 
    string += random.choice(part3) + " "
    if (random.choice([True, True, False])):
            string += random.choice(part4) + " "
    string += random.choice(part5)
    return string

def get_event():
    '''generate misc event'''

    part1 = ["Enjoying", "Considering", "Furious about", "Enduring", 
            "Criticizing", "Planning", "Dressing for", "Shopping for", 
            "Watching", "At", "Attending", "Arriving to", "Leaving", 
            "Suffering through", "Home from", "Going to", "Heading to", 
            "Finalizing", "Paying for", "Arranging", "Preparing", 
            "Organizing"]
    part2 = ["my", "this", "this", "this", "that", "Richard's", "some", 
            "the", "the", "the", "the", "the"]
    part3 = ["ridiculous", "first-class", "charitable", "fundraising",
            "European", "infuriating", "black tie", "atrocious", 
            "prestigious", "country club", "elite", "sophisticated", 
            "unsophisticated", "charity", "alumni", "transatlantic", 
            "producers'", "18th century", "antique"]
    part4 = ["DAR", "rare books", "rare manuscripts", "tea", "golf", 
            "foie gras", "champagne", "art", "painting", "sculpture", 
            "wine", "jewelry", "ballet", "opera", "symphony"]
    part5 = ["meeting", "exhibit", "exhibition", "auction", "acution", 
            "conference", "lecture", "museum opening", "estate sale", 
            "premiere", "debut"]
    string = random.choice(part1) + " " + random.choice(part2) + " "
    if (random.choice([True, False, False])):
            string += random.choice(part3) + " "
    string += random.choice(part4) + " " + random.choice(part5)
    return string

def get_activity():
    '''randomly pick event type from weighted distribution'''

    pick = random.choice([0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2])
    if pick == 0:
        return get_sport()
    elif pick == 1:
        return get_party()
    else:
        return get_event()

def get_tag():
    '''return random hashtag'''

    part1 = ["OldMoney", "DAR", "GilmoreGirls", "Netflix", "Yale", 
            "PoolHouse", "NewMaid", "TwoGlassesOfWine", "Worldly", 
            "ViciousTrollop", "DrugDealersTakeTheBus", 
            "BrusselsSproutFetish", "PanicRoom", "Paris", "EmilyGilmore", 
            "GilmoreGuys", "BirkinBag", "JohnKeithPaulBingo",
            "WeddingBellBlues", "MissCeline", "Hartford", "Connecticut", 
            "Chilton", "StarsHollow", "VenetianApples", "WhereYouLead", 
            "LukesDiner", "TeamLogan", "Gilmore", "SeasonEight", 
            "PersonalShopper", "Mojito", "OpenForBusiness", 
            "BishopIsQueen", "SalmonPuffs", "DoYouYahoo", "Tracksuit",
            "FridayNightDinner", "June3rd", "MuchoMacAndCheese", "ShaqWho",
            "InCones", "MarriageJug", "BaggingTheSwede"]
    return str(random.choice(part1))

def get_string():
    '''generate full tweet text'''

    activity = get_activity() + " with "
    name = get_first() + get_middle() +  " " + get_last()
    tag1 = " #" + get_tag()
    tag2 = " #" + get_tag()
    while tag1 == tag2:
        tag2 = " #" + get_tag()
    return str(activity + name + tag1 + tag2)

def go_tweet():
    '''generate, record and send tweet'''

    twitter = TwitterAPI()
    to_tweet = get_string()
    print(str(datetime.datetime.now()) + " " + to_tweet)
    twitter.tweet(to_tweet)
 

if __name__ == '__main__':

    go_tweet()

