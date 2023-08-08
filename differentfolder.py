import os
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

def changesInFolders(folderPath1, folderPath2):
    changedFiles = []
    totalAddedLinesCount = 0
    totalDeletedLines_count = 0

    for root, _, files in os.walk(folderPath1):
        for file in files:
            filePath1 = os.path.join(root, file)
            filePath2 = os.path.join(folderPath2, file)
            
            if os.path.exists(filePath2):
                added, deleted, modified, addedLinesCount, deleted_lines_count = findChangesSolidity(filePath1, filePath2)
                totalAddedLinesCount += addedLinesCount
                totalDeletedLines_count += deleted_lines_count
                if added or deleted or modified:
                    changedFiles.append((file, added, deleted, modified))

    return changedFiles, totalAddedLinesCount, totalDeletedLines_count

# Example usage:
folderPath1 = './solidity-examples - Copy/solidity-examples-master/examples'
folderPath2 = './solidity-examples/solidity-examples-master/examples'
changedFiles, totalAddedLines, totalDeletedLines = changesInFolders(folderPath1, folderPath2)

for file, added, deleted, modified in changedFiles:
    print(f"File: {file}")
   
    if added:
        print("Added Lines:")
        for lineNum, lineText in added:
            print(f"Line {lineNum}: {lineText}")

    if deleted:
        print("Deleted Lines:")
        for lineNum, lineText in deleted:
            print(f"Line {lineNum}: {lineText}")

    print()
    
print(f"Total number of added lines in all files: {totalAddedLines}")
print(f"Total number of deleted lines in all files: {totalDeletedLines}")
print(f"Total number of changes: {totalAddedLines + totalDeletedLines}")