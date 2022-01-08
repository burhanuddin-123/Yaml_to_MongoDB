import yaml
import json
import os
import pandas as pd
# Importing Connection class from connection module
from connection import Connection

with open("335982.yaml") as infile:
    os_list = yaml.load(infile, Loader=yaml.FullLoader)

# Create the connection table object which will create the connection client and database
myconn = Connection()

# Converting multiple yaml into json
# How to select file from path
for file in os.listdir():
    if file.endswith(".yaml"):
        with open(file) as infile:
            os_list = yaml.load(infile, Loader=yaml.FullLoader)
        
        filename = file.split(".")[0]
        
        # create the collection by giving name
        myconn.create_collection(filename)

        single_inning = {}
        innings = os_list["innings"] # Will list all the innings
        count = 0
        for index in range(len(innings)):
            for key in innings[index].keys():
                single_inning["innings"] = key
                single_inning["team"] = innings[index][key]["team"]
                deliveries = innings[index][key]["deliveries"]
                for index in range(len(deliveries)):
                    for key in deliveries[index].keys():
                        delivery = deliveries[index][key]
                        single_inning["delivery_no"] = str(key)
                        single_inning.update(delivery)
                        
                        # Creating a unique id
                        final_filename = filename+"_"+str(count+1)
                        single_inning["_id"] = final_filename
                        
                        # inserting the final record to database
                        myconn.insert_one_records(single_inning)

                        ## Transferring the object into json using dumps method
                        json_object = json.dumps(single_inning, indent=4)
                        ## Writing the json object to file.
                        final_filename = filename+"_"+str(count+1)
                        with open("json/"+final_filename+".json", "w") as outfile:
                            outfile.write(json_object)
                        count = count+1



####################################################
# Converting 1 yaml file into multiple json

## Dynamically
# single_inning = {}
# innings = os_list["innings"] # Will list all the innings
# count = 0
# for index in range(len(innings)):
#     for key in innings[index].keys():
#         single_inning["innings"] = key
#         single_inning["team"] = innings[index][key]["team"]
#         deliveries = innings[index][key]["deliveries"]
#         for index in range(len(deliveries)):
#             for key in deliveries[index].keys():
#                 delivery = deliveries[index][key]
#                 single_inning["delivery_no"] = str(key)
#                 single_inning.update(delivery)

#                 ## Transferring the object into json using dumps method
#                 json_object = json.dumps(single_inning, indent=4)
#                 ## Writing the json object to file.
#                 with open("json/335982_"+str(count+1)+".json", "w") as outfile:
#                     outfile.write(json_object)
#                 count = count+1


################################################################
## Statically Separting
# for index in range(len(innings)):
#     if index==0:
#         first_innings = innings[index]["1st innings"] # separting 1 innings
#     else:
#         second_innings = innings[index]["2nd innings"] # separting 2 innings



# For 1st innings
# team = first_innings["team"]
# deliveries = first_innings["deliveries"]

# single_delivery = {}
# single_delivery["innings"] = "1st"
# single_delivery["team"] = team
# for index in range(len(deliveries)):
#     for key in deliveries[index].keys():
#         delivery = deliveries[index][key]
#         single_delivery["delivery_no"] = key
#         single_delivery.update(delivery)
#         print(single_delivery)
#         json_object = json.dumps(single_delivery, indent=4)
#         with open("json/335982_"+str(index+1)+".json", "w") as outfile:
#             outfile.write(json_object)


# # For 2nd innings
# team = second_innings["team"]
# deliveries = second_innings["deliveries"]
# single_delivery = {}
# single_delivery["innings"] = "2nd"
# single_delivery["team"] = team
# for index in range(len(deliveries)):
#     for key in deliveries[index].keys():
#         delivery = deliveries[index][key]
#         single_delivery["delivery_no"] = key
#         single_delivery.update(delivery)
#         print(single_delivery)
#         json_object = json.dumps(single_delivery, indent=4)
#         with open("json/335982_"+str(index+1)+".json", "w") as outfile:
#             outfile.write(json_object)
