f = open("test.txt", "w")
f.write("This is our file.\n here we talk about  how programming works.\n Be confident and  focus  on the your goal.")
f.close()

f = open("object.txt", "w")
f.write('Line 1')
f.write('Line 2')
f.write('Line 3')
f.close ()

f = open("data.txt" ,"w")
lines = ["Line 1", "Line 2 ", "Line 3"]
f.writelines(lines)
f.close()

import csv

my_game = [ "Emily","England","Eagle"," Earbuds"]
with open("game.csv" , "w" ,newline ="") as csvfile:
      my_writer = csv.writer(csvfile , delimiter = ",")
      my_writer.writerow(my_game)