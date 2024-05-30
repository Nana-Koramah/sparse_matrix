#!/usr/bin/env python3

class SparseMatrix:
    def __init__(self, numRows, numCols):
        self.numRows = numRows
        self.numCols = numCols
        self.data = {}

    def load_from_file(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if len(lines) < 3:
                raise ValueError("File does not contain enough lines.")
            try:
                self.numRows = int(lines[0].split('=')[1])
                self.numCols = int(lines[1].split('=')[1])
            except IndexError:
                raise ValueError("File format is incorrect. Expected 'rows=x' and 'cols=y' on the first two lines.")
            for line in lines[2:]:
                row, col, value = map(int, line.strip().strip('()').split(','))
                self.set_element(row, col, value)

    def set_element(self, row, col, value):
        self.data[(row, col)] = value

    def get_element(self, row, col):
        return self.data.get((row, col), 0)

    def add(self, other):
        result = SparseMatrix(self.numRows, self.numCols)
        for (row, col), value in self.data.items():
            result.set_element(row, col, value + other.get_element(row, col))
        return result

    def subtract(self, other):
        result = SparseMatrix(self.numRows, self.numCols)
        for (row, col), value in self.data.items():
            result.set_element(row, col, value - other.get_element(row, col))
        return result

def process_matrices(input_file_path):
    # Load the first matrix
    matrix1 = SparseMatrix(5, 5)
    matrix1.load_from_file(input_file_path)

    # Load the second matrix
    matrix2 = SparseMatrix(5, 5)
    matrix2.load_from_file(input_file_path)

    # List of operations to perform
    operations = ["add", "subtract"]

    for operation in operations:
        # Perform the operation
        if operation == "add":
            result = matrix1.add(matrix2)
        elif operation == "subtract":
            result = matrix1.subtract(matrix2)
        else:
            print(f"Unsupported operation: {operation}")
            continue

        # Save the result to the output file
        output_file_path = f'output_{operation.lower()}.txt'
        with open(output_file_path, 'w') as file:
            file.write(f"Operation: {operation.capitalize()}\n")
            file.write(f"rows={result.numRows}\ncols={result.numCols}\n")
            for (row, col), value in result.data.items():
                file.write(f"{row},{col},{value}\n")

if __name__ == "__main__":
    input_file_path = 'sample_input_01.txt'
    process_matrices(input_file_path)

