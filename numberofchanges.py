import difflib

def findChangesSolidity(filePath1, filePath2):
    try:
        with open(filePath1, 'r') as file1, open(filePath2, 'r') as file2:
            file1Lines = file1.readlines()
            file2Lines = file2.readlines()

            differ = difflib.Differ()
            diff = list(differ.compare(file1Lines, file2Lines))

            added_lines = []
            deleted_lines = []
            modified_lines = []

            addedLinesCount=0 
            deletedLinesCount=0 
            modifiedLinesCount=0

            for i,line in enumerate(diff, 1):
                if(line.startswith('+ ')):
                    addedLinesCount+=1
                    added_lines.append((i, line[2:]))
                elif line.startswith('- '):
                    deletedLinesCount+=1
                    deleted_lines.append((i, line[2:]))
                else:
                    modifiedLinesCount+=1
                    modified_lines.append((i, line[2:]))

            return added_lines, deleted_lines, modified_lines, addedLinesCount, deletedLinesCount, modifiedLinesCount
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return [], [], [], 0, 0, 0

# Example usage:
filePath1 = './sample.sol'
filePath2 = './sample1.sol'
added, deleted, modified, addedLinesCount, deletedLinesCount, modifiedLinesCount = findChangesSolidity(filePath1, filePath2)

print(f"Added number of lines: {addedLinesCount}")
print(f"Deleted number of lines: {deletedLinesCount}")
print(f"Total number of changes:{addedLinesCount+deletedLinesCount}")

print("Added Lines:")
for line_num, line_text in added:
    print(f"Line : {line_text}")

print("\nDeleted Lines:")
for line_num, line_text in deleted:
    print(f"Line : {line_text}")



