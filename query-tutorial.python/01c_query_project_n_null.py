from common import *

##projection ref. https://docs.mongodb.com/manual/tutorial/project-fields-from-query-results/
"""use **project** to specify or restrict fields to return"""

#projection on simple/nested fields
qc=db.inventory.find({"status": "A"}                                                ); mongo_print(qc, count=True)
qc=db.inventory.find({"status": "A"}, {"_id":0}                                     ); mongo_print(qc) #all but _id
qc=db.inventory.find({"status": "A"}, {"item":1, "status":1}                        ); mongo_print(qc) #item, status only
qc=db.inventory.find({"status": "A"}, {"item":1, "status":1, "_id":0}               ); mongo_print(qc) #item, status only, excluding _id
qc=db.inventory.find({"status": "A"}, {"item":1, "status":1, "_id":0, "size.uom":1} ); mongo_print(qc)

#projection on array
qc=db.inventory.find({"status": "A"}, {"item":1                            }); mongo_print(qc) #
qc=db.inventory.find({"status": "A"}, {"item":1, "instock": {"$slice": -1} }); mongo_print(qc) #last item of array via $slice



##check for empty/null ref. https://docs.mongodb.com/manual/tutorial/query-for-null-fields/
qc=db.inventory.find({"item": None}                   ); mongo_print(qc, count=True)
qc=db.inventory.find({"instock": None}                ); mongo_print(qc, count=True)
qc=db.inventory.find({"instock": {"$exists": False}  }); mongo_print(qc, count=True)
qc=db.inventory.find({"instock": {"$exists": True}   }); mongo_print(qc, count=True)

#TODO What is diff. between None and $exists:False ?
