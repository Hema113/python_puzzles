
def read_text(file_name):
    num_lines = 0
    num_words = 0
    num_chars = 0

    with open(file_name, 'r') as f:
        for line in f:
            words = line.split()

            num_lines += 1
            num_words += len(words)
            num_chars += len(line)
        return num_lines, num_words ,num_chars

if __name__ == "__main__":
    file_name = "sample.txt"
    print("No of sentence>words>chars:", read_text(file_name))























"""def read_file(inp):
    count =[]
    new_file=inp.readlines()
    word_count = new_file.spilt()
    count=len(word_count)
    return count

if __name__ == "__main__":
    file_name = "sample.txt"
    inp = open(file_name ,'r')
    print("words>>", read_file(inp))"""



"""def read_text_file(file_name):
    count = []
    with open(file_name,'r') as new_file:
        file_data = new_file.read()
        new_file.seek(0)

        # print(file_data)

        words_count = file_data.split()
        s_count = new_file.readlines()

        # print(s_count)

        count.append(len(file_data))
        count.append(len(words_count))
        count.append(len(s_count))

    return count

# Main Function

if __name__ == "__main__":
    file_name = 'open.txt' # input("Enter file name to read it >>>")
    count = read_text_file(file_name)
    print("Selected file : ",file_name)
    print("No of sentence : ", count[2])
print("No of words :", count[1])
print("no of char:", count[0]-1)"""
