from common import *

db.users.delete_many({}) #clear all first

##do seeding
db.users.insert_many([
    {
      "_id"    : "ruby han",
      "joined" : datetime.strptime("2016-04-04", "%Y-%m-%d"),
      "likes"  : ["youtube for kids"],
    },

    {
      "_id"    : "jane",
      "joined" : datetime.strptime("2011-01-02", "%Y-%m-%d"),
      "likes"  : ["golf", "racquetball"],
    },

    {
      "_id"    : "joe",
      "joined" : datetime.strptime("2012-06-08", "%Y-%m-%d"),
      "likes"  : ["tennis", "golf", "swimming"],
    },

    {
      "_id"    : "jill",
      "joined" : datetime.strptime("2012-06-02", "%Y-%m-%d"),
      "likes"  : ["tennis", "golf", "swimming"],
    },
    {
      "_id"    : "jack",
      "joined" : datetime.strptime("2012-06-02", "%Y-%m-%d"),
      "likes"  : ["tennis", "golf", "swimming"],
    },

])

#output
mongo_print(query_cursor=db.users.find())
