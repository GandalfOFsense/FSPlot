import time

noun1 = ""
noun2 = ""
verb1 = ""
adj = ""
adj2 = ""

print("__FSPlot__")
time.sleep(1)
print("This is Funny Story Plotter.")
time.sleep(2)
print("Time to start!")
time.sleep(1)
noun1 = input("Write a noun: "+noun1)
verb1 = input("Write a verb: "+verb1)
noun2 = input("Write a noun: "+noun2)
adj = input("Write a adjective: "+adj)
adj2 = input("Write a another one adjective: "+adj2)
print(" ")

print("__Your story__:")
print("Have you ever thought that you would be a "+str(noun1.capitalize())+"?")
print("You will have to "+str(verb1.lower())+" the rabbit.")
print("And also, visit the "+str(noun2.capitalize())+".")
print("And then, sleep with a "+str(adj.lower())+" girl.")
print("This is such a "+str(adj2.lower())+" story.")
input("^_^")