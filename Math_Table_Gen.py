# MATHS TABLE MAKER FROM 0 TO INFINITY
print("A PROJECT BY CODE INDIA\nINSTAGRAM - '@CODE_INDIA_OFFICIAL'\nYOUTUBE - 'CODE INDIA- DHANANJAY ARNE'\n")
print("WELCOME TO MATHS TABLE GENERATOR\n")
table_num = input("WHICH NUMBER TABLE DO YOU WANT?\n")
print("\n")
from_to = input(f"GENERATE {table_num} TABLE FROM \n{table_num} x 1 \nto \n{table_num} x ")
print("\n")
print(f"HERE IS YOUR {table_num} Table..")
for i in range(int(from_to)):
    i = i + 1
    product = int(table_num) * i
    print(f"{table_num} x {i} = {product}")
print("THANK YOU FOR USING MY PROGRAM!!")
