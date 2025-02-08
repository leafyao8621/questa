CPP = g++
CPPFLAGS = -Wall -Wextra -Werror -pedantic
LIBS = -llemon
SRC = $(wildcard src/*.cpp) $(wildcard src/*/*.cpp) $(wildcard src/*/*/*.cpp)
OBJ = $(SRC:.cpp=.o)
BIN = questa

%.o: %.cpp
	$(CPP) -g -c $(CPPFLAGS) $< -o $@

$(BIN): $(OBJ)
	$(CPP) $(OBJ) -o $(BIN) $(LIBS)

.PHONY: clean valgrind
clean:
	@rm $(OBJ)
	@rm $(BIN)
valgrind: $(BIN)
	@valgrind -s --leak-check=full ./$(BIN)
