CPP = g++
CPPFLAGS = -Wall -Wextra -Werror -pedantic
LIBS = -llemon
LFLAGS = -pthread
SRC = $(wildcard src/*.cpp) $(wildcard src/*/*.cpp) $(wildcard src/*/*/*.cpp)
OBJ = $(SRC:.cpp=.o)
BIN = questa

%.o: %.cpp
	$(CPP) -O3 -c $(CPPFLAGS) $< -o $@

$(BIN): $(OBJ)
	$(CPP) $(OBJ) -o $(BIN) $(LIBS) $(LFLAGS)

.PHONY: clean valgrind
clean:
	@rm $(OBJ)
	@rm $(BIN)
valgrind: $(BIN)
	@valgrind -s --leak-check=full ./$(BIN)
