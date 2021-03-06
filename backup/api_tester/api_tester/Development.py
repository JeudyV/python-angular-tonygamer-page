import os
import json
import requests

def test():
    return {'hello': 'world'} 

def data_params(player, platfor):
    return { 'player': player, 'platfor': platfor }

def order_book():
    return[
    {   
        'platform':'xbox',
        'name':'Ninja',
        'views':'32.000',
        'warzone':{
            'lvl':'13',
            'win':'1',
            'top_5':'4.000',
            'top_10':'4.000',
            'top_25':'4.000',
            'KD_Ratio':'464516',
            'Damage_game':'564616',
            'kills':'4.000',
            'Deaths':'4.000',
            'Downs':'4.000',
            'Avg_life':'4.000',
            'score':'4.000',
            'score_min':'4.000',
            'score_game':'4.000',
            'cash':'4.000',
            'contracts':'4.000',
            'win_por':'4.000'
        },
        'battle':{
            'lvl':'13',
            'win':'1',
            'top_5':'4.000',
            'top_10':'4.000',
            'top_25':'4.000',
            'KD_Ratio':'464516',
            'Damage_game':'564616',
            'kills':'4.000',
            'Deaths':'4.000',
            'Downs':'4.000',
            'Avg_life':'4.000',
            'score':'4.000',
            'score_min':'4.000',
            'score_game':'4.000',
            'cash':'4.000',
            'contracts':'4.000',
            'win_por':'4.000'
        }
        
    }
    ]

def data_table():
     return {
      "data": [
        {
            "id": "1",
            "name": 'ADX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "2",
            "name": 'aaa',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "3",
            "name": 'ssss',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "4",
            "name": 'ddd',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "5",
            "name": 'fff',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "6",
            "name": 'ggg',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "7",
            "name": 'hhhh',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "8",
            "name": 'assas',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "9",
            "name": 'adsds',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "10",
            "name": 'dwdas',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "11",
            "name": 'ADfffccX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "12",
            "name": '12121',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "13",
            "name": 'dfcsd',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "14",
            "name": 'tfds',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "15",
            "name": 'vsdfwe',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "16",
            "name": 'sefse',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "17",
            "name": 'sefsefe',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "18",
            "name": 'sefsef',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "19",
            "name": 'AgtrergDX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "20",
            "name": 'ADX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "21",
            "name": 'ADX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "22",
            "name": 'ADX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "23",
            "name": 'ADX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "24",
            "name": 'ADX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "25",
            "name": 'ADX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "26",
            "name": 'ADX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "27",
            "name": 'ADX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "28",
            "name": 'ADX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "29",
            "name": 'ADX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "30",
            "name": 'ADX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "31",
            "name": 'ADX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "32",
            "name": 'ADX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "33",
            "name": 'ADX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "34",
            "name": 'ADX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "35",
            "name": 'ADX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "36",
            "name": 'ADX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "37",
            "name": 'ADX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "38",
            "name": 'ADX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "39",
            "name": 'ADX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
        {
            "id": "40",
            "name": 'ADX',
            "stock": "AMZN",
            "status": "starting",
            "type": "long",
            "Rating": 'A',
            "return": "320 800",
            "annual_return": "97%",
            "risk_reward": "N/A",
            "batting_AVG": "75%",
            "AVG": "29%"
        },
      ]
    }

def data_table2( player ):

    return {
          "name": player
        }