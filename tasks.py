# -*- coding: utf-8 -*-
from invoke import run, task
import pymongo


@task 
def seed():
  db = pymongo.MongoClient(host="mongo").containers
  for i in """Biscuit icing ice cream pastry. Gingerbread muffin soufflé croissant sweet roll. Marzipan chupa chups sweet roll candy canes brownie cookie macaroon lemon drops jujubes. Soufflé danish gummi bears cake. Cheesecake dessert donut muffin pie. Dragée sesame snaps cake cupcake topping danish tootsie roll jelly. Lemon drops powder dragée jelly beans pastry lemon drops dessert fruitcake pie. Biscuit lollipop cookie tiramisu sesame snaps caramels candy canes. Bonbon tart ice cream cake jelly beans. Brownie bear claw ice cream lemon drops sesame snaps fruitcake carrot cake. Tiramisu cake cotton candy bear claw pudding. Fruitcake gummi bears brownie. Wafer jelly-o sugar plum carrot cake cake pie caramels soufflé.""".split():
    db.Containers.insert({"name": i})


@task
def drop():
  db = pymongo.MongoClient(host="mongo").containers
  db.Containers.drop()
  
