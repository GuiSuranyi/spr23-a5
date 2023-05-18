calculator: main.o division.o addition.o multiplication.o subtraction.o
	cc -o calculator main.o division.o addition.o multiplication.o subtraction.o
 


division.o addition.o multiplication.o subtraction.o: operations.h

main.o:

objects =  division.o addition.o multiplication.o subtraction.o


clean:
	rm -f calculator $(objects) main.o

.PHONY: clean


