import sqlite3
import json
from sqlite3 import Error

try:
    sql = sqlite3.connect("Database.db")
    connection = sql.cursor()
    print("Database connection is started")
except Error:
    print("Error: ", Error)


docks = connection.execute("select * from docks").fetchall()

stations = connection.execute("select * from station").fetchall()

json_data_1= []
json_data_2= []

for dock in docks:
    near_station = dock[3]
    for station in stations:
        if station[2] == near_station:
            goal = f's{station[0]}_goal'
            goal = {
                    "pose": {
                        "header": {
                            "frame_id": station[2]
                        },
                        "pose": {
                            "position": {
                                "x": station[11],
                                "y": station[12],
                                "z": 0.0
                            },
                            "orientation": {
                                "x": 0.0,
                                "y": 0.0,
                                "z": station[7],
                                "w": station[8]
                            }
                        }
                    },
                    "behavior_tree": "",
            }

            initial_pose = {
                "header": {
                    "frame_id": dock[2]
                },
                "pose": {
                    "pose": {
                        "position": {
                            "x": dock[10],
                            "y": dock[11],
                            "z": 0.0
                        },
                        "orientation": {
                            "x": 0.0,
                            "y": 0.0,
                            "z": dock[6],
                            "w": dock[7]
                        }
                    },
                    "covariance": [
                        0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                        0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                        0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                        0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                        0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                        0.0, 0.0, 0.0, 0.0, 0.0, 0.0
                    ]
                }
            }
            data = {
                "goal": goal,
                "initial_pose": initial_pose
            }
            json_data_1.append(data)
    else:
        if dock[3] =='':
            goal = {
                "pose": {
                    "header": {
                        "frame_id": dock[2]
                    },
                    "pose": {
                        "position": {
                            "x": dock[10],
                            "y": dock[11],
                            "z": 0.0
                        },
                        "orientation": {
                            "x": 0.0,
                            "y": 0.0,
                            "z": dock[6],
                            "w": dock[7]
                        }
                    }
                },
                "behavior_tree": "",
            }
            data2 = {
                "goal":goal
            }
            json_data_2.append(data2)


with open('data.json', 'w') as outfile:
    json.dump(json_data_1, outfile, ensure_ascii=True, indent=4)

with open('goal.json', 'w') as outfile:
    json.dump(json_data_2, outfile, ensure_ascii=True, indent=4)