class Reverse:
    def __init__(self, input_string):
        self.input_string = input_string

    def reverse_words(self):
        return ' '.join(self.input_string.split()[::-1])

reverse = Reverse("codingal is cool")
print(reverse.reverse_words())
