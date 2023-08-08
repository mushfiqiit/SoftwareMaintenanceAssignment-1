def countSLOC(filePath):
    try:
        with open(filePath, 'r') as file:
            lines = file.readlines()
            lineCount=0
            for line in lines:
                if(line.strip() and not line.strip().startswith('//')):
                    lineCount+=1
            return lineCount
    except FileNotFoundError:
        print(f"Error: File '{filePath}' was not found.")
        return 0


# Usage
filePath = './sample.sol'
lineCount = countSLOC(filePath)
print(f"Source Line of Code: {lineCount}")