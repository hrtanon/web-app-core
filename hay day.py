import random
import os
import time as daytime


crops={
    "psenice":{"name":"psenice"
    ,"cost":"3"
    ,"odolnost":"výborná"
    ,"prodeh":"9"
    ,"days":"3"},
    
    "zemák": {"name": "zemáčik"
    ,"cost":"6"
    ,"odolnost":"neuveritelná"
    ,"prodej":"26"
    ,"days":"6"},
    
    "hlávkobé zelí":{"name":"zelé",
    "cost":"10"
    ,"odolnost":"pochybná"
    ,"prodej":"66"
    ,"days":"4"},
    
    "jablon":{"name":"jablecny strom",
    "cost":"99,3"
    ,"odolnost":"stromovitá 1"
    ,"prodej":"6"
    ,"days":"2"
    ,"rust": "7"}
}


pocasi={
    "sunny":{"name":"sunny", "rust":1, "risk": 0,"weight":0.35},
    "cloudy":{"name":"zatateno", "rust":1,"risk":0,"weight":0.35},
    "storm":{"name":"bourka","rust": 0,"risk":2,"weight":0.045},
    "drought":{"name":"suco","rust": 0 ,"risk":1,"weight":0.10},
    "rain":{"name":"prehanky","rust":2,"risk":0,"weight":0.15},
    "ufo":{"name":"prilet ufa","rust":0,"risk":100,"weight":0.005}
    }



def pocasi_vyber(pocasi):
    pocasis=list(pocasi.keys())
    weight=[pocasi[x]["weight"] for x in pocasis]
    wether=random.choices(pocasis,weight)
    print(wether)
    return wether
pocasi_vyber(pocasi)