# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    with open("story.txt", "r") as file:
        content = file.read()
        file.close()
        return content


def count_words():

    # calling the first function
    # the output of read_file_content() is used for count_words()
    text = read_file_content("story.txt")

    # creating an empty dictionary to hold words and number of occurences
    count = {}

    # using for loop for iteration
    text = text.rstrip()
    word = text.split()
    for i in word:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count


# function call
print(count_words())
