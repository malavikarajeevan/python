
""""sigle inheritance"""
# class vehicle:
#     color="red"
#     def engine(self):
#         print("all vehicles have engine")
# class car(vehicle):
#     def fourwheel(self):
#         print("car have four wheel",self.color)
# c=car()
# c.fourwheel()
# c.engine()

"""multilevel inheritance"""
# class grandpa:
#     def kashandi(self):
#         print("kashandi family")
#     def farmer(self):
#         print("farmer")
# class father(grandpa):
#     def driver(self):
#         print("driver")
#     def reader(self):
#         print("reader")
# class me(father):
#     def swimming(self):
#         print("swimming")
#     def engineer(self):
#         print("engineer")
# class mechild(me):
#     def gamer(self):
#         print("gamer")
# ob=father()
# ob.reader()

"""""multiple inheritance"""
# class father:
#     def driver(self):
#         print("driver")
# class mother:
#     def cook(self):
#         print("cook")
# class girl(father,mother):
#     def engineer(self):
#         print("engineer")
# g=girl()
# g.cook()
# g.driver()